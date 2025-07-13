# ProjetoMicro

O projeto consiste em uma automatização do controle de uma casa inteligente com Home Assistant, a partir do reconhecimento de gestos feitos por um sabre.

## Componentes utilizados

1) ESP 32
2) 2 botões
4) Impressão 3D para corpo do sabre
5) Lampada LED inteligente

## Esquemático eletronico
<img width="1493" height="1244" alt="esquematico" src="https://github.com/user-attachments/assets/8693a985-b5f9-4bce-88cc-3d8041f68f5c" />

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

2) /esp32-lightsaber-main: Código do esp utilizado

3) /voice_code: Código python para comandos de voz do home assistant

## Telas da interface

1) Tela inicial

![image](https://github.com/user-attachments/assets/070faaf7-96c9-489e-af7a-dcfdbc5fd613)

2) Tela da gravação de novo movimento

![image](https://github.com/user-attachments/assets/86433e74-e78b-4ac4-b4bb-f328e8390270)

3) Tela de cadastro de movimento

![image](https://github.com/user-attachments/assets/ffc5e93a-55fe-4936-a0c9-adb4245e3eed)

4) Tela de histórico de gestos

![image](https://github.com/user-attachments/assets/97110a36-8820-40b0-bc2b-b986a8a79b68)



