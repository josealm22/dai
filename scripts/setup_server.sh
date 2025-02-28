#!/bin/bash
set -e

# Variables
SERVICE_NAME="gunicorn"
USER="adminzuc"  # Asegúrate de reemplazar con tu usuario real
WORKING_DIR="/home/adminzuc/proyects/dai"
VENV_DIR="$WORKING_DIR/venv"
APP_MODULE="web:app"

# Instalar dependencias
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install -y python3 python3-pip python3-venv git ansible

# Crear entorno virtual si no existe
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR"
fi

# Activar entorno virtual e instalar dependencias
source "$VENV_DIR/bin/activate"
pip install -r "$WORKING_DIR/requirements.txt"
python3 generate_secret_token.py 


# Crear archivo de servicio systemd
SERVICE_FILE="/etc/systemd/system/$SERVICE_NAME.service"

echo "Creando el servicio systemd en $SERVICE_FILE"

sudo bash -c "cat > $SERVICE_FILE" <<EOF
[Unit]
Description=Gunicorn daemon for Flask App
After=network.target

[Service]
User=$USER
Group=www-data
WorkingDirectory=$WORKING_DIR
ExecStart=$VENV_DIR/bin/gunicorn --workers 3 --bind 0.0.0.0:5005 $APP_MODULE
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Recargar systemd y habilitar el servicio
echo "Recargando systemd y habilitando el servicio..."
sudo systemctl daemon-reload
sudo systemctl enable $SERVICE_NAME
sudo systemctl restart $SERVICE_NAME

# Verificar que Gunicorn está corriendo
sudo systemctl status $SERVICE_NAME --no-pager
