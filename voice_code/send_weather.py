#!/usr/bin/env python3
"""
Script simples para enviar solicitação de clima via MQTT
"""

import paho.mqtt.client as mqtt
import json
import sys
from config import *

def send_weather_request():
    """Envia solicitação de clima via MQTT"""
    
    # Criar cliente MQTT
    client = mqtt.Client()
    client.username_pw_set(MQTT_USER, MQTT_PASS)
    
    try:
        # Conectar ao broker
        print(f"Conectando ao broker {MQTT_BROKER}...")
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        
        # Mensagem para solicitar clima
        message = {
            "action": "get_weather",
            "location": CITY
        }
        
        # Publicar mensagem
        result = client.publish(MQTT_TOPIC_TEMPO, json.dumps(message))
        result.wait_for_publish()
        
        print(f"✅ Solicitação de clima enviada para {CITY}!")
        print("🎧 O sistema deve falar as informações do clima em alguns segundos...")
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False
    
    finally:
        client.disconnect()
    
    return True

if __name__ == "__main__":
    print("🌤️ Enviando solicitação de clima via MQTT...")
    send_weather_request() 