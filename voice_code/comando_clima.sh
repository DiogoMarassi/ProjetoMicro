#!/bin/bash

# Script para enviar solicitação de clima via MQTT
# Uso: ./comando_clima.sh

echo "Enviando solicitação de clima para Rio de Janeiro..."

# Ativar ambiente virtual e executar script
source venv/bin/activate
python send_weather.py

echo "Comando executado!" 