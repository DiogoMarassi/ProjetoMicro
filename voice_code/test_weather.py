#!/usr/bin/env python3
"""
Script de teste para verificar a funcionalidade do clima
"""

import pyttsx3
import requests
from datetime import datetime
from config import *

def test_weather_api():
    """Testa a API do clima usando OpenMeteo (gratuita, sem chave)"""
    print("Testando API do clima (OpenMeteo)...")
    
    try:
        url = f"https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": LATITUDE,
            "longitude": LONGITUDE,
            "current": "temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m,weather_code",
            "timezone": "America/Sao_Paulo"
        }
        
        print(f"Buscando clima para: {CITY} ({LATITUDE}, {LONGITUDE})")
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        current = data["current"]
        
        # Extrair informações
        temperature = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        feels_like = current["apparent_temperature"]
        wind_speed = current["wind_speed_10m"]
        weather_code = current["weather_code"]
        
        # Converter código do clima para descrição
        weather_descriptions = {
            0: "clear sky",
            1: "mainly clear",
            2: "partly cloudy",
            3: "overcast",
            45: "foggy",
            48: "depositing rime fog",
            51: "light drizzle",
            53: "moderate drizzle",
            55: "dense drizzle",
            61: "slight rain",
            63: "moderate rain",
            65: "heavy rain",
            71: "slight snow",
            73: "moderate snow",
            75: "heavy snow",
            77: "snow grains",
            80: "slight rain showers",
            81: "moderate rain showers",
            82: "violent rain showers",
            85: "slight snow showers",
            86: "heavy snow showers",
            95: "thunderstorm",
            96: "thunderstorm with slight hail",
            99: "thunderstorm with heavy hail"
        }
        
        description = weather_descriptions.get(weather_code, "unknown weather")
        
        current_time = datetime.now().strftime("%H:%M")
        
        # Formatar mensagem
        weather_message = f"Current weather in {CITY} at {current_time}: {description}. Temperature is {temperature:.1f} degrees Celsius, feels like {feels_like:.1f} degrees. Humidity is {humidity} percent. Wind speed is {wind_speed} kilometers per hour."
        
        print("API do clima funcionando!")
        print(f"Dados recebidos:")
        print(f"   - Temperatura: {temperature:.1f}°C")
        print(f"   - Sensação térmica: {feels_like:.1f}°C")
        print(f"   - Umidade: {humidity}%")
        print(f"   - Vento: {wind_speed} km/h")
        print(f"   - Descrição: {description}")
        print(f"   - Código do clima: {weather_code}")
        
        return weather_message
        
    except requests.RequestException as e:
        print(f"Erro na API: {e}")
        return False
    except KeyError as e:
        print(f"Erro ao processar dados: {e}")
        return False

def test_tts(message):
    """Testa o sistema de text-to-speech"""
    print("\nTestando sistema de fala...")
    
    try:
        tts = pyttsx3.init()
        
        # Configurar TTS
        tts.setProperty('rate', TTS_RATE)
        tts.setProperty('volume', TTS_VOLUME)
        
        # Tentar definir voz em inglês
        voices = tts.getProperty('voices')
        for voice in voices:
            if 'english' in voice.name.lower() or 'en' in voice.id.lower():
                tts.setProperty('voice', voice.id)
                print(f"🎙️ Voz selecionada: {voice.name}")
                break
        
        print("Falando mensagem de teste...")
        tts.say("Testing the voice system. This is a test message.")
        tts.runAndWait()
        
        print("Sistema de fala funcionando!")
        
        # Falar informações do clima
        if message:
            print("Falando informações do clima...")
            tts.say(message)
            tts.runAndWait()
            print("Informações do clima faladas com sucesso!")
        
        return True
        
    except Exception as e:
        print(f"Erro no sistema de fala: {e}")
        return False

def main():
    """Função principal"""
    print("Iniciando testes do sistema...")
    
    # Testar API do clima
    weather_message = test_weather_api()
    
    # Testar sistema de fala
    tts_success = test_tts(weather_message)
    
    print("\n" + "="*50)
    if weather_message and tts_success:
        print("Todos os testes passaram! Sistema funcionando corretamente.")
    else:
        print("Alguns testes falharam. Verifique as configurações.")
    print("="*50)

if __name__ == "__main__":
    main() 