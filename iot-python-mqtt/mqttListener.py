# ------------------------------------------
# --- Desenvolvedor.: Alysson Morandi
# --- Data..........: 21/01/2022
# --- Objetivo......: Cria o listener do topico no broker remoto e mantem executando
# --- Python Version: 3.8
# ------------------------------------------

import paho.mqtt.client as mqtt
import ssl
from mqttDataToDB import sensor_data

# MQTTs Settings
MQTT_Broker = "<Your HiveMQ Cloud Broker>"
MQTT_Port = <port>
Keep_Alive_Interval = 45
MQTT_Topic = "<your_topic>/#"
ClientID = "<Your_ClientID>"
Username = "<Your_username>"
Password = "<Your_Password>"

# Subscribe em todos os topicos do topico base
def on_connect(mosq, obj, flags, rc):
    client.subscribe(MQTT_Topic, qos=0)
    print("CONNACK received with code %s." % rc)    

# Captura e salva a msg na base de dados
def on_message(mosq, obj, msg):
    print("Recebido no Topico: " + msg.topic)
    print(msg.payload)
    # chama a função para gravação dos dados na base
    sensor_data(msg.payload)

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

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
