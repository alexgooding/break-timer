#!/bin/bash

### Execute script within venv ###

# clean previous build
echo "CLEANING WORKSPACE"
rm -rf build
rm -rf dist

# create db
echo "CREATING POSTGRES DATABASE"
python manage.py makemigrations break_timer
python manage.py migrate
python3 manage.py loaddata muteAudio.json

# create executable
echo "CREATING BREAK-TIMER EXECUTABLE"
pip install pyinstaller
pyinstaller --name=break-timer manage.py --onefile
