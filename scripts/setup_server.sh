#!/bin/bash
set -e

# Instalar dependencias
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    git \
    ansible

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Iniciar servidor Flask
gunicorn --bind 0.0.0.0:5005 web.app:app