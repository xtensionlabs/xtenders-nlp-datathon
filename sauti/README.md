# Sauti · Kiswahili assistant

Sauti uses the team's AfriBERTa model to interpret a Kiswahili request and explain what it understood.

## Run in Colab

Open [NLP_Project.ipynb](https://colab.research.google.com/drive/1_Zz6qY-MJbF5CKRsMzEESwLqzGEHT9Xo#scrollTo=gng68AWYvVr0) and run **Open the Sauti app**. Colab pulls the current Sauti code and downloads the team's [checkpoint](https://drive.google.com/file/d/1mDaxe4d0g2KACrkVW4vOgnzX01sjXNux/view) as needed. The chat appears below the cell.

## Run on Windows

From the repository root, run these commands in PowerShell. Use Python 3.11 or newer with PyTorch support.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r sauti/requirements.txt
New-Item -ItemType Directory -Force models
.\.venv\Scripts\gdown.exe 1mDaxe4d0g2KACrkVW4vOgnzX01sjXNux -O models/joint_model.pt
.\.venv\Scripts\python.exe sauti/sauti.py --repo . --checkpoint models/joint_model.pt
```

Open [Sauti on localhost](http://127.0.0.1:8000/) once the server is ready. The first startup fetches AfriBERTa's configuration and tokenizer. The checkpoint stays in the ignored `models/` directory.

Run the app tests from inside `sauti/` with `python -m unittest discover -s tests`.
