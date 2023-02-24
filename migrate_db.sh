#!/bin/bash

python manage.py makemigrations break_timer
python manage.py migrate
