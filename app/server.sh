#!/bin/bash
pwd
DJANGODIR=$(cd `dirname $0` && pwd)
pwd
DJANGO_SETTINGS_MODULE=app.settings
pwd
source env/bin/activate
pwd
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
pwd
exec python manage.py runserver 0:9000

read -p "Presiona Enter para salir..."


