# ProjetoMicro

🛰️ Sabre: Reconhecimento de Gestos e automatização controle de casa inteligente com Home Assistant.
O Sabre é um sistema modular e extensível para automação pessoal baseado em gestos, com comunicação em tempo real via MQTT. Projetado para funcionar com sensores de movimento (como acelerômetros) e múltiplas linguagens e contextos, o Sabre permite executar ações como tocar playlists no Spotify, exibir clima, ou acionar rotinas com base em gestos configuráveis.

Funcionalidades
1) Reconhecimento de gestos personalizados

2) Integração com APIs externas (ex: clima, Spotify)

3) Cadastro e mapeamento semântico de significados para gestos

4) Comunicação em tempo real via MQTT

5) Organização modular por idioma, gênero e contexto

6) Sistema de playlists e rotinas configuráveis

7) Notificações visuais e sonoras programáveis

📡 Arquitetura
css
Copiar
Editar
[Dispositivo Sensorial] --> [MQTT Broker] <---> [Servidor Python Flask]
                                          ↘
                                    [Serviços Externos (APIs)]
MQTT: protocolo leve de publicação/assinatura usado para troca de mensagens em tempo real.

Servidor Python: recebe gestos, interpreta comandos, consulta e aciona APIs.

Cliente sensor: envia gestos reconhecidos via MQTT.

APIs integradas: clima, player de mídia (Spotify), entre outros.

🧠 Conceito de Gesto
Cada gesto é definido por:

json
Copiar
Editar
{
  "gesto": "gesto_exemplo",
  "significado": "toca_playlist",
  "genero": "masculino",
  "idioma": "pt-br",
  "cor": "#FFAA00",
  "playlist": "spotify_playlist_id"
}
Ações como toca_playlist, notifica_tempo, envia_mensagem, etc., são interpretadas pelo sistema.