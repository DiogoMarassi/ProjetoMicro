# ProjetoMicro

Sabre: Reconhecimento de Gestos e automatização controle de casa inteligente com Home Assistant.
O Sabre é um sistema modular e extensível para automação pessoal baseado em gestos, com comunicação em tempo real via MQTT. Projetado para funcionar com sensores de movimento (como acelerômetros) e múltiplas linguagens e contextos, o Sabre permite executar ações como tocar playlists no Spotify, exibir clima, ou acionar rotinas com base em gestos configuráveis.

## Funcionalidades

1) Reconhecimento de gestos personalizados, a partir de um acelerômetro no sabre.

2) Representação visual a partir de cores no sabre, selecionadas na interface

3) Representação auditiva de comandos do Home Assistant, com possibilidade de 2 idiomas selecionados na interface

4) Integração com API do Spotify, possibilitando escolher um genero de música a ser tocada como um gesto

5) Cadastro, visualização e histórico de gestos

6) Comunicação em tempo real via MQTT

## Comunicações MQTT

Temos 2 brokers, um do Home Assitant e um da Interface usando WebSocket para atualização de gesto em tempo real.

## Códigos

1) /interfaceProjetoMicro: Código python da interface completa do projeto. Recebe gestos, interpreta comandos, consulta e aciona APIs e comunicações MQTT.

2) /esp32-lightsaber-main: Código do arduino

3) /voice_code: Código python para comandos de voz do home assistant

## Conceito de Gesto
Cada gesto é definido por:

```json
{
  "gesto": "gesto_exemplo",
  "significado": "toca_playlist",
  "genero": "pagode",
  "idioma": "pt",
  "cor": "vermelho",
  "playlist": "spotify_playlist_id"
}
```

Ações como toca_playlist, notifica_tempo, envia_mensagem, etc., são interpretadas pelo sistema.
