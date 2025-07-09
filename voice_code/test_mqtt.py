#!/usr/bin/env python3
"""
Script de teste para enviar mensagens MQTT para testar o sistema de voz
"""

import paho.mqtt.client as mqtt
import json
import time
from config import *

def on_connect(client, userdata, flags, rc):
    """Callback quando conecta ao broker MQTT"""
    if rc == 0:
        print("✅ Conectado ao broker MQTT!")
    else:
        print(f"❌ Falha na conexão. Código: {rc}")

def on_publish(client, userdata, mid):
    """Callback quando uma mensagem é publicada"""
    print(f"✅ Mensagem publicada com sucesso! (ID: {mid})")

def test_voice_message():
    """Testa o tópico de mensagens de voz"""
    print("\n🎤 Testando tópico 'notifica/voz'...")
    
    # Mensagem de teste
    message = {
        "mensagem": "Hello! This is a test message from the MQTT voice system."
    }
    
    # Publicar mensagem
    result = client.publish(MQTT_TOPIC_VOZ, json.dumps(message))
    result.wait_for_publish()
    
    print(f"📤 Mensagem enviada para {MQTT_TOPIC_VOZ}: {message['mensagem']}")

def test_weather_message():
    """Testa o tópico de informações do clima"""
    print("\n🌤️ Testando tópico 'notifica/tempo'...")
    
    # Mensagem de teste para solicitar clima
    message = {
        "action": "get_weather",
        "timestamp": time.time()
    }
    
    # Publicar mensagem
    result = client.publish(MQTT_TOPIC_TEMPO, json.dumps(message))
    result.wait_for_publish()
    
    print(f"📤 Mensagem enviada para {MQTT_TOPIC_TEMPO}: Solicitação de informações do clima")

def main():
    """Função principal de teste"""
    global client
    
    print("🚀 Iniciando testes do sistema MQTT de voz...")
    print(f"📍 Broker: {MQTT_BROKER}:{MQTT_PORT}")
    print(f"👤 Usuário: {MQTT_USER}")
    
    # Criar cliente MQTT
    client = mqtt.Client()
    client.username_pw_set(MQTT_USER, MQTT_PASS)
    client.on_connect = on_connect
    client.on_publish = on_publish
    
    try:
        # Conectar ao broker
        print(f"\n🔌 Conectando ao broker {MQTT_BROKER}...")
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        
        # Iniciar loop em background
        client.loop_start()
        
        # Aguardar conexão
        time.sleep(2)
        
        # Testar mensagem de voz
        test_voice_message()
        time.sleep(3)  # Aguardar processamento
        
        # Testar mensagem do clima
        test_weather_message()
        time.sleep(3)  # Aguardar processamento
        
        print("\n✅ Testes concluídos!")
        print("🎧 Verifique se o sistema principal (main.py) falou as mensagens.")
        
    except Exception as e:
        print(f"❌ Erro durante o teste: {e}")
    
    finally:
        # Limpar
        client.loop_stop()
        client.disconnect()
        print("\n🔌 Desconectado do broker MQTT")

if __name__ == "__main__":
    main() 