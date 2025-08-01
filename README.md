# tron_app

To run app follow commands

git clone <repo>

python -m venv env

### For Windows
env\Scripts\python -m pip install -r requirements.txt 

### For Linux
env/bin/python -m pip install -r requirements.txt

and finally

env\Scripts\python -m uvicorn --port 8080 main:app