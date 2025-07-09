import paho.mqtt.client as mqtt
import pyttsx3
import json
import requests
from datetime import datetime
from config import *

tts = pyttsx3.init()

# Configure TTS settings
tts.setProperty('rate', TTS_RATE)
tts.setProperty('volume', TTS_VOLUME)

# List available voices for debugging
print("[TTS] Available voices:")
voices = tts.getProperty('voices')
for i, voice in enumerate(voices):
    print(f"  {i}: {voice.name} ({voice.id})")

# Try to find the best voices for English and Portuguese
english_voice_id = None
portuguese_voice_id = None

for voice in voices:
    voice_name_lower = voice.name.lower()
    voice_id_lower = voice.id.lower()
    
    # Look for English voices
    if english_voice_id is None and ('english' in voice_name_lower or 'en' in voice_id_lower or 'alex' in voice_name_lower):
        english_voice_id = voice.id
        print(f"[TTS] Found English voice: {voice.name}")
    
    # Look for Portuguese voices
    if portuguese_voice_id is None and ('portuguese' in voice_name_lower or 'pt' in voice_id_lower or 'joana' in voice_name_lower or 'brazil' in voice_name_lower):
        portuguese_voice_id = voice.id
        print(f"[TTS] Found Portuguese voice: {voice.name}")

# Set default voice to English if found, otherwise use first available
if english_voice_id:
    tts.setProperty('voice', english_voice_id)
    print(f"[TTS] Set default voice to English")
else:
    if voices:
        tts.setProperty('voice', voices[0].id)
        print(f"[TTS] Set default voice to: {voices[0].name}")

def get_weather_info_english():
    """Get current weather information in English using OpenMeteo API"""
    try:
        url = f"https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": LATITUDE,
            "longitude": LONGITUDE,
            "current": "temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m,weather_code",
            "timezone": "America/Sao_Paulo"
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        current = data["current"]
        
        # Extract weather information
        temperature = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        feels_like = current["apparent_temperature"]
        wind_speed = current["wind_speed_10m"]
        weather_code = current["weather_code"]
        
        # Convert weather code to description
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
        
        # Get current time
        current_time = datetime.now().strftime("%H:%M")
        
        # Format the weather message in English
        weather_message = f"Current weather in {CITY} at {current_time}: {description}. Temperature is {temperature:.1f} degrees Celsius, feels like {feels_like:.1f} degrees. Humidity is {humidity} percent. Wind speed is {wind_speed} kilometers per hour."
        
        return weather_message
        
    except requests.RequestException as e:
        return f"Error getting weather information: {str(e)}"
    except KeyError as e:
        return f"Error parsing weather data: {str(e)}"

def get_weather_info_portuguese():
    """Get current weather information in Portuguese using OpenMeteo API"""
    try:
        url = f"https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": LATITUDE,
            "longitude": LONGITUDE,
            "current": "temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m,weather_code",
            "timezone": "America/Sao_Paulo"
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        current = data["current"]
        
        # Extract weather information
        temperature = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        feels_like = current["apparent_temperature"]
        wind_speed = current["wind_speed_10m"]
        weather_code = current["weather_code"]
        
        # Convert weather code to Portuguese description
        weather_descriptions = {
            0: "céu limpo",
            1: "predominantemente limpo",
            2: "parcialmente nublado",
            3: "nublado",
            45: "nebuloso",
            48: "névoa com geada",
            51: "chuvisco leve",
            53: "chuvisco moderado",
            55: "chuvisco intenso",
            61: "chuva leve",
            63: "chuva moderada",
            65: "chuva forte",
            71: "neve leve",
            73: "neve moderada",
            75: "neve forte",
            77: "grãos de neve",
            80: "chuva leve",
            81: "chuva moderada",
            82: "chuva forte",
            85: "neve leve",
            86: "neve forte",
            95: "trovoada",
            96: "trovoada com granizo leve",
            99: "trovoada com granizo forte"
        }
        
        description = weather_descriptions.get(weather_code, "clima desconhecido")
        
        # Get current time
        current_time = datetime.now().strftime("%H:%M")
        
        # Format the weather message in Portuguese
        weather_message = f"Clima atual em {CITY} às {current_time}: {description}. Temperatura de {temperature:.1f} graus Celsius, sensação térmica de {feels_like:.1f} graus. Umidade de {humidity} por cento. Velocidade do vento de {wind_speed} quilômetros por hora."
        
        return weather_message
        
    except requests.RequestException as e:
        return f"Erro ao obter informações do clima: {str(e)}"
    except KeyError as e:
        return f"Erro ao processar dados do clima: {str(e)}"

def get_weather_info():
    """Get current weather information using OpenMeteo API (free, no API key required)"""
    # Default to English for backward compatibility
    return get_weather_info_english()

def speak_message(message, language="en"):
    """Speak a given message using TTS with appropriate voice for the language"""
    try:
        print(f"[TTS] Speaking in {language}: {message}")
        
        # Configure voice based on language
        if language == "pt" and portuguese_voice_id:
            # Use Portuguese voice if available
            tts.setProperty('voice', portuguese_voice_id)
            print(f"[TTS] Using Portuguese voice")
        elif language == "en" and english_voice_id:
            # Use English voice if available
            tts.setProperty('voice', english_voice_id)
            print(f"[TTS] Using English voice")
        else:
            # Use current voice (default)
            print(f"[TTS] Using current voice")
        
        tts.say(message)
        tts.runAndWait()
    except Exception as e:
        print(f"[TTS ERROR] {e}")
        # Try to speak with default voice as fallback
        try:
            print("[TTS] Trying fallback with default voice...")
            tts.say(message)
            tts.runAndWait()
        except Exception as e2:
            print(f"[TTS FALLBACK ERROR] {e2}")

def on_message(client, userdata, msg):
    """Handle incoming MQTT messages based on topic"""
    try:
        topic = msg.topic
        payload = msg.payload.decode()
        
        print(f"[MQTT] Received message on topic {topic}: {payload}")
        
        if topic == MQTT_TOPIC_VOZ:
            # Handle voice notification - speak the message
            try:
                payload_data = json.loads(payload)
                mensagem = payload_data.get("mensagem", payload)
            except json.JSONDecodeError:
                mensagem = payload
                
            speak_message(mensagem)
            
        elif topic == MQTT_TOPIC_TEMPO:
            # Handle weather notification - get and speak weather info based on language
            payload_lower = payload.lower().strip()
            
            if payload_lower == "pt":
                # Speak weather in Portuguese
                weather_info = get_weather_info_portuguese()
                speak_message(weather_info, "pt")
            elif payload_lower == "en":
                # Speak weather in English
                weather_info = get_weather_info_english()
                speak_message(weather_info, "en")
            else:
                # Default to English for backward compatibility
                weather_info = get_weather_info_english()
                speak_message(weather_info, "en")
            
        else:
            print(f"[MQTT] Unknown topic: {topic}")
            
    except Exception as e:
        error_msg = f"Error processing message: {str(e)}"
        print(f"[ERROR] {error_msg}")
        speak_message(error_msg)

client = mqtt.Client()
client.username_pw_set(MQTT_USER, MQTT_PASS)
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.subscribe(MQTT_TOPIC_VOZ)
client.subscribe(MQTT_TOPIC_TEMPO)

print(f"[MQTT] Listening for messages on topics:")
print(f"  - {MQTT_TOPIC_VOZ}: Speak custom messages")
print(f"  - {MQTT_TOPIC_TEMPO}: Speak weather information")
client.loop_forever()