#!/bin/bash

python manage.py makemigrations break_timer
python manage.py migrate
python manage.py loaddata muteAudio.json
