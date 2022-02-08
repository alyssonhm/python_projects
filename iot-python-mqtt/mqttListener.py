# ------------------------------------------
# --- Desenvolvedor.: Alysson Morandi
# --- Data..........: 21/01/2022
# --- Objetivo......: Cria o listener do topico no broker remoto e mantem executando para recepção dos dados dos sensores
# --- Python Version: 3.8
# ------------------------------------------

import paho.mqtt.client as mqtt
import ssl
from mqttDataToDB import sensor_data

# MQTTs Settings
MQTT_Broker = 'your-broker.s1.eu.hivemq.cloud' #HiveMQ Cloud
MQTT_Port = 8883
Keep_Alive_Interval = 45
MQTT_Topic = '/sensors/#'
ClientID = 'TesteMQTTPython'
Username = 'username'
Password = 'password'

# Subscribe em todos os topicos do topico base
def on_connect(mosq, obj, flags, rc):
    client.subscribe(MQTT_Topic, qos=0)
    print(f'CONNACK received with code {rc}')    

# Captura e salva a msg na base de dados
def on_message(mosq, obj, msg):
    print(f'Recebido no Topico: {msg.topic}')
    print(msg.payload)
    # chama a função para gravação dos dados na base
    sensor_data(msg.payload)

def on_subscribe(mosq, obj, mid, granted_qos):
    print(f'Subscribed:  {mid} qos: {granted_qos}')

# instancia variavel para mqtt client
client = mqtt.Client(ClientID)

# set username e password para acesso ao broker no HiveMQ
client.username_pw_set(Username, Password)

# habilita TLS para conexão segura
client.tls_set(tls_version=ssl.PROTOCOL_TLS)

# Definindo eventos de callbacks
client.on_message = on_message
client.on_connect = on_connect
client.on_subscribe = on_subscribe

# Connect
client.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

# loop
client.loop_forever()