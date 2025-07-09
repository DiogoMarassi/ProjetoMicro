# Weather API Configuration
# Using OpenMeteo API (free, no API key required)
WEATHER_API_KEY = None  # Not needed for OpenMeteo
CITY = "Rio de Janeiro"  # City name
COUNTRY_CODE = "BR"  # Country code (ISO 3166-1 alpha-2)

# Coordinates for São Paulo (OpenMeteo uses coordinates)
LATITUDE = -22.9201
LONGITUDE = -43.0811

# MQTT Configuration
MQTT_BROKER = "192.168.0.100"
MQTT_PORT = 1883
MQTT_TOPIC_VOZ = "notifica/voz"  # Topic for custom voice messages
MQTT_TOPIC_TEMPO = "notifica/tempo"  # Topic for weather information
MQTT_USER = "mqttuser"
MQTT_PASS = "1234"

# Text-to-Speech Configuration
TTS_RATE = 120  # Speech rate (words per minute)
TTS_VOLUME = 1.0  # Volume (0.0 to 1.0) 