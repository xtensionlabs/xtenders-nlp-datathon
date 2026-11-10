"""Render Sauti in a Colab output cell and load the team's Drive checkpoint."""

from importlib.util import find_spec, module_from_spec, spec_from_file_location
from pathlib import Path
import subprocess
import sys


APP = Path(__file__).resolve().parent
TEAM_REPO = APP.parent
MODEL_REVISION = "b630cb3ee42c4c6f9a45194094b4d3e95b835bd3"
CHECKPOINT_ID = "1mDaxe4d0g2KACrkVW4vOgnzX01sjXNux"


def open_demo():
    from google.colab import output
    from IPython.display import HTML, JSON, display

    dependencies = ("transformers", "seqeval", "sentencepiece", "gdown")
    missing = [package for package in dependencies if find_spec(package) is None]
    if missing:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", *missing], check=True)

    import gdown

    runtime_files = Path("/content/sauti-runtime")
    runtime_files.mkdir(exist_ok=True)
    checkpoint = runtime_files / "joint_model.pt"
    previous_checkpoint = Path("/content/xtenders-nlp-datathon/models/joint_model.pt")
    if previous_checkpoint.is_file():
        checkpoint = previous_checkpoint
    elif not checkpoint.is_file():
        print("Downloading the team checkpoint (503 MB)...")
        if gdown.download(id=CHECKPOINT_ID, output=str(checkpoint), resume=True) is None:
            raise RuntimeError("The checkpoint download failed. Run the cell again to retry.")

    # Keep the architecture and label ordering tied to this specific checkpoint.
    for filename in ("train_joint_intent_slot.py", "metrics_and_errors.json"):
        content = subprocess.check_output(
            ["git", "-C", str(TEAM_REPO), "show", f"{MODEL_REVISION}:{filename}"]
        )
        (runtime_files / filename).write_bytes(content)

    spec = spec_from_file_location("sauti_colab_model", APP / "sauti_model.py")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    print("Loading the Sauti model...")
    respond = module.load_responder(runtime_files, checkpoint)

    def reply(message):
        if not isinstance(message, str) or not 1 <= len(message.strip()) <= 280:
            return JSON({"error": "Andika ombi lenye herufi 1 hadi 280."})
        return JSON({"reply": respond(message.strip())})

    output.register_callback("sauti.reply", reply)

    web = APP / "web"
    html = (web / "index.html").read_text(encoding="utf-8")
    styles = (web / "app.css").read_text(encoding="utf-8")
    script = (web / "app.js").read_text(encoding="utf-8")
    layout = html[html.index("<header"):html.index("<script src=")]
    # The same UI sends requests through Colab's kernel callback in this environment.
    bridge = """
    window.sautiReply = async (message, signal) => {
      const response = google.colab.kernel.invokeFunction("sauti.reply", [message], {});
      const cancelled = new Promise((_, reject) => {
        signal.addEventListener("abort", () => reject(new Error("Request cancelled")), {once: true});
      });
      const output = await Promise.race([response, cancelled]);
      return output.data["application/json"];
    };
    """
    display(HTML(f"<style>{styles}</style>{layout}<script>(() => {{ {bridge}\n{script} }})();</script>"))


if __name__ == "__main__":
    open_demo()
