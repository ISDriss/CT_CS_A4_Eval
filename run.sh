python3 -m venv .venv
#source .venv/Scripts/activate      #only for filthy bash + windows users
source .venv/bin/activate
pip install -r requirements.txt
fastapi dev server.py