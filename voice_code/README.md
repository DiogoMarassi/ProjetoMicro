# Sistema de Notificação por Voz com Clima

Este sistema escuta mensagens MQTT em dois tópicos diferentes e responde falando informações personalizadas ou dados do clima em tempo real em inglês.

## Funcionalidades

- **Tópico `notifica/voz`**: Fala mensagens personalizadas enviadas via MQTT
- **Tópico `notifica/tempo`**: Fala informações do clima atual em inglês
- Text-to-speech em inglês
- Configuração centralizada
- Tratamento de erros robusto
- **API do clima gratuita** (OpenMeteo - sem necessidade de chave)

## Instalação

### 1. Instalar Dependências

```bash
# Ativar ambiente virtual
source venv/bin/activate

# Instalar pacotes necessários
pip install paho-mqtt pyttsx3 requests
```

### 2. Configurar o Sistema

Edite `config.py` para personalizar:

- **Localização**: Altere `LATITUDE` e `LONGITUDE` para sua localização desejada
- **Configurações MQTT**: Atualize endereço do broker, porta, credenciais se necessário
- **Configurações TTS**: Ajuste velocidade e volume da fala

### 3. Executar o Sistema

```bash
python main.py
```

O sistema irá:
- Conectar ao broker MQTT
- Escutar mensagens nos tópicos configurados
- Quando uma mensagem for recebida:
  - **`notifica/voz`**: Falar a mensagem personalizada
  - **`notifica/tempo`**: Buscar e falar informações do clima atual

## Como Usar

### Enviar Mensagem Personalizada
Publique no tópico `notifica/voz`:
```json
{
  "mensagem": "Hello, this is a custom message"
}
```

### Solicitar Informações do Clima
Publique qualquer mensagem no tópico `notifica/tempo`:
```json
{
  "action": "get_weather"
}
```

## Configurações

### API do Clima (OpenMeteo - Gratuita)
- **Sem chave de API necessária!**
- `LATITUDE`: Latitude da localização (ex: -23.5505 para São Paulo)
- `LONGITUDE`: Longitude da localização (ex: -46.6333 para São Paulo)
- `CITY`: Nome da cidade (apenas para exibição)

### Configurações MQTT
- `MQTT_BROKER`: Endereço do broker MQTT
- `MQTT_PORT`: Porta do broker MQTT
- `MQTT_TOPIC_VOZ`: Tópico para mensagens de voz personalizadas
- `MQTT_TOPIC_TEMPO`: Tópico para informações do clima
- `MQTT_USER`: Usuário MQTT
- `MQTT_PASS`: Senha MQTT

### Text-to-Speech
- `TTS_RATE`: Velocidade da fala em palavras por minuto
- `TTS_VOLUME`: Nível de volume (0.0 a 1.0)

## Informações do Clima Fornecidas

O sistema fala os seguintes detalhes meteorológicos:
- Hora atual
- Descrição do clima (baseada em códigos WMO)
- Temperatura (real e sensação térmica)
- Percentual de umidade
- Velocidade do vento em km/h

## Exemplo de Saída

**Mensagem personalizada:**
"Hello, this is a custom message"

**Informações do clima:**
"Current weather in São Paulo at 14:30: partly cloudy. Temperature is 22.5 degrees Celsius, feels like 24.1 degrees. Humidity is 65 percent. Wind speed is 12.3 kilometers per hour."

## Vantagens da API OpenMeteo

- ✅ **Completamente gratuita**
- ✅ **Sem necessidade de chave de API**
- ✅ **Dados meteorológicos precisos**
- ✅ **Sem limites de requisições**
- ✅ **Dados em tempo real**
- ✅ **Cobertura global**

## Solução de Problemas

1. **Erro de Conexão**: Verifique se tem conexão com a internet
2. **Localização Incorreta**: Verifique as coordenadas no `config.py`
3. **Problemas com TTS**: Verifique se pyttsx3 está instalado e configurado corretamente
4. **Conexão MQTT**: Certifique-se de que o broker MQTT está rodando e acessível

## Dependências

- `paho-mqtt`: Biblioteca cliente MQTT
- `pyttsx3`: Biblioteca text-to-speech
- `requests`: Biblioteca HTTP para chamadas de API 