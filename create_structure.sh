#!/bin/bash

# Definir la estructura de directorios
DIRS=(
    "web"
    "web/routes"
    "web/templates"
    "web/static/css"
    "web/static/js"
    "web/utils"
    "ansible/playbooks"
    "ansible/inventory"
    "scripts"
)

# Definir los archivos a crear
FILES=(
    "web/app.py"
    "web/config.py"
    "web/models.py"
    "web/routes/auth.py"
    "web/routes/playbooks.py"
    "web/routes/deployments.py"
    "web/routes/clients.py"
    "web/routes/__init__.py"
    "web/templates/base.html"
    "web/templates/login.html"
    "web/templates/playbooks.html"
    "web/templates/deployments.html"
    "web/templates/clients.html"
    "web/static/css/styles.css"
    "web/static/js/ace-editor.js"
    "web/static/js/main.js"
    "web/utils/ansible_runner.py"
    "web/utils/helpers.py"
    "ansible/inventory/dynamic_inventory.py"
    "scripts/setup_server.sh"
    "scripts/client_linux.sh"
    "scripts/client_windows.ps1"
    "requirements.txt"
    "README.md"
)

# Crear los directorios
for dir in "${DIRS[@]}"; do
    mkdir -p "$dir"
    echo "Directorio creado: $dir"
    
done

# Crear los archivos
for file in "${FILES[@]}"; do
    touch "$file"
    echo "Archivo creado: $file"
done

echo "Estructura de proyecto creada con éxito."
