#!/bin/bash
set -e  # Detiene la ejecución si hay un error

# Ruta absoluta de la aplicación y el entorno virtual
APP_DIR="/home/f4lk0n/unitygov/app"
VENV_DIR="$APP_DIR/env"

cd "$APP_DIR"
pwd  # Verificar la ubicación actual

# Definir la variable de configuración de Django
export DJANGO_SETTINGS_MODULE=app.settings

# Activar el entorno virtual con una ruta absoluta
source "$VENV_DIR/bin/activate"

# Mostrar la ubicación de Python para verificar que está dentro del entorno virtual
which python

# Ejecutar el servidor Django
exec python manage.py runserver 0.0.0.0:9000

