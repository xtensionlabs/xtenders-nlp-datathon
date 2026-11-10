import json
from http.server import HTTPServer
from threading import Thread
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from sauti import handler_for
from sauti_model import format_reply


class SautiTests(unittest.TestCase):
    def setUp(self):
        self.seen = []

        def respond(message):
            self.seen.append(message)
            if message == "hitilafu":
                raise RuntimeError("model temporarily unavailable")
            return format_reply("alarm_set", [{"type": "time", "value": "saa moja asubuhi"}])

        self.server = HTTPServer(("127.0.0.1", 0), handler_for(respond))
        self.thread = Thread(target=self.server.serve_forever)
        self.thread.start()
        self.url = f"http://127.0.0.1:{self.server.server_port}"
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.thread.join)
        self.addCleanup(self.server.shutdown)

    def post(self, payload):
        request = Request(self.url + "/api/reply", data=json.dumps(payload).encode(),
                          headers={"Content-Type": "application/json"})
        return urlopen(request, timeout=3)

    def test_interface_and_plain_language_reply(self):
        with urlopen(self.url, timeout=3) as response:
            self.assertIn(b'id="composer"', response.read())
        with self.post({"message": "  Weka kengele saa moja asubuhi. "}) as response:
            self.assertEqual(json.load(response), {
                "reply": "Nimeelewa kuwa unataka kuweka kengele.\nMuda: saa moja asubuhi",
            })
        self.assertEqual(self.seen, ["Weka kengele saa moja asubuhi."])

    def test_invalid_input_does_not_reach_model(self):
        for value in ("   ", "a" * 281, 123):
            with self.subTest(value=value), self.assertRaises(HTTPError) as error:
                self.post({"message": value})
            self.assertEqual(error.exception.code, 400)
            error.exception.close()
        self.assertFalse(self.seen)

    def test_model_failure_returns_retryable_error(self):
        with self.assertLogs(level="ERROR"), self.assertRaises(HTTPError) as error:
            self.post({"message": "hitilafu"})
        self.assertEqual(error.exception.code, 503)
        with error.exception as response:
            self.assertIn("Jaribu tena", json.load(response)["error"])
