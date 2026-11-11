const welcome = document.querySelector("#welcome");
const conversation = document.querySelector("#conversation");
const thread = document.querySelector("#thread");
const form = document.querySelector("#composer");
const input = document.querySelector("#message");
const send = document.querySelector("#send");
const status = document.querySelector("#status");
const newChat = document.querySelector("#new-chat");
const theme = document.querySelector("#theme");
let pending = null;

function updateSend() {
  send.disabled = Boolean(pending) || !input.value.trim();
}

async function fetchReply(message, signal) {
  const response = await fetch("/api/reply", {
    method: "POST", headers: {"Content-Type": "application/json"},
    body: JSON.stringify({message}), signal,
  });
  if (!response.ok) throw new Error("Reply unavailable");
  return response.json();
}

async function requestReply(message, turn) {
  if (pending) return;
  const request = new AbortController();
  pending = request;
  conversation.dataset.thinking = "";
  status.textContent = "Sauti inasoma ombi lako…";
  updateSend();
  const timer = setTimeout(() => request.abort(), 45000);
  const answer = document.createElement("p");
  answer.className = "answer";
  const label = document.createElement("strong");
  label.textContent = "Sauti";
  try {
    const replyService = window.sautiReply ?? fetchReply;
    const result = await replyService(message, request.signal);
    if (typeof result?.reply !== "string") throw new Error("Reply unavailable");
    if (pending !== request) return;
    answer.append(label, document.createTextNode(result.reply));
    turn.append(answer);
    if (result.frame && typeof result.frame === "object") {
      const frameOutput = document.createElement("section");
      frameOutput.className = "frame-output";
      frameOutput.setAttribute("aria-label", "Muundo wa matokeo ya modeli");
      const caption = document.createElement("p");
      caption.className = "frame-caption";
      caption.textContent = "Muundo uliotambuliwa (JSON ya modeli; unaweza kukosea)";
      const json = document.createElement("pre");
      json.textContent = JSON.stringify(result.frame, null, 2);
      frameOutput.append(caption, json);
      turn.append(frameOutput);
    }
    if (navigator.clipboard) {
      const copy = document.createElement("button");
      copy.type = "button";
      copy.className = "copy-reply";
      copy.textContent = "Nakili jibu";
      copy.addEventListener("click", async () => {
        try {
          await navigator.clipboard.writeText(result.reply);
          copy.textContent = "Jibu limenakiliwa";
        } catch {
          copy.textContent = "Kunakili kumeshindikana";
        }
      });
      turn.append(copy);
    }
  } catch {
    if (pending !== request) return;
    answer.append(label, document.createTextNode("Jibu halikupatikana. Tafadhali jaribu tena."));
    const retry = document.createElement("button");
    retry.type = "button";
    retry.className = "retry";
    retry.textContent = "Jaribu tena";
    retry.addEventListener("click", () => {
      if (pending) return;
      answer.remove();
      retry.remove();
      requestReply(message, turn);
    });
    turn.append(answer, retry);
  } finally {
    clearTimeout(timer);
    if (pending === request) {
      pending = null;
      delete conversation.dataset.thinking;
      status.textContent = "";
      updateSend();
    }
  }
}

input.addEventListener("input", updateSend);
document.querySelectorAll("[data-prompt]").forEach(button => {
  button.addEventListener("click", () => {
    input.value = button.dataset.prompt;
    updateSend();
    input.focus();
  });
});

form.addEventListener("submit", event => {
  event.preventDefault();
  const message = input.value.trim();
  if (!message || pending) return;
  welcome.hidden = true;
  conversation.hidden = false;
  newChat.hidden = false;
  const turn = document.createElement("div");
  turn.className = "turn";
  const question = document.createElement("p");
  question.className = "question";
  question.textContent = message;
  turn.append(question);
  thread.append(turn);
  input.value = "";
  input.focus();
  requestReply(message, turn);
});

newChat.addEventListener("click", () => {
  pending?.abort();
  pending = null;
  delete conversation.dataset.thinking;
  thread.replaceChildren();
  conversation.hidden = true;
  welcome.hidden = false;
  newChat.hidden = true;
  status.textContent = "";
  input.value = "";
  updateSend();
  input.focus();
});

const darkMode = matchMedia("(prefers-color-scheme: dark)");
function setTheme(dark) {
  document.documentElement.style.colorScheme = dark ? "dark" : "light";
  theme.setAttribute("aria-pressed", String(dark));
  theme.setAttribute("aria-label", dark ? "Tumia mandhari meupe" : "Tumia mandhari meusi");
}
setTheme(darkMode.matches);
theme.addEventListener("click", () => setTheme(theme.getAttribute("aria-pressed") === "false"));
