@echo off
echo Vekil AL baslatiliyor...
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
python app.py
