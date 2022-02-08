
# ------------------------------------------
# --- Desenvolvedor.: Alysson Morandi
# --- Data..........: 29/01/2022
# --- Objetivo......: Publica dados ficticios para o tópico definido em MQTT_Topic
# --- Python Version: 3.8
# ------------------------------------------

import paho.mqtt.client as mqtt
import random, threading, json
from datetime import datetime
import ssl

# MQTTs Settings
MQTT_Broker = 'your-broker.s1.eu.hivemq.cloud' #HiveMQ Cloud
MQTT_Port = 8883
Keep_Alive_Interval = 45
MQTT_Topic = '/sensors/data'
ClientID = 'TesteMQTTPython'
Username = 'username'
Password = 'password'

def on_connect(client, userdata, flags, rc):
    print(f'CONNACK received with code {rc}')

def on_publish(client, userdata, mid):
    print(f'messageId: {mid}')

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print(f'Desconectado: {rc}')

def on_log(client, userdata, level, buf):
    print('log: ',buf)    

client = mqtt.Client(ClientID)
# set username e password para acesso ao broker no HiveMQ
client.username_pw_set(Username, Password)

# habilita TLS para conexão segura
client.tls_set(tls_version=ssl.PROTOCOL_TLS)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.on_log = on_log

# Conectando
client.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

def publish_To_Topic(topic, message):
    client.publish(topic, message, qos=0)
    print(f'Message: {message}')
    print('')

def publish_Fake_Sensor_Values_to_MQTT():
    threading.Timer(3.0, publish_Fake_Sensor_Values_to_MQTT).start()

    Temperatura_Fake_Value = float('{0:.2f}'.format(random.uniform(10, 42)))
    Umidade_Fake_Value = float('{0:.2f}'.format(random.uniform(20, 100)))

    # faz um random no dict com sensorId e o Local do sensor
    sensor_local = {'sensor1':'sala', 'sensor2':'quarto', 'sensor3':'escritorio'}
    sensorid, location = random.choice(list(sensor_local.items()))       

    Json_Data = {}
    Json_Data['SensorID'] = sensorid
    Json_Data['Location'] = location
    Json_Data['DateTime'] = (datetime.now()).strftime('%d/%m/%Y %H:%M:%S')
    Json_Data['Temperatura'] = Temperatura_Fake_Value
    Json_Data['Umidade'] = Umidade_Fake_Value

    sensor_json_data = json.dumps(Json_Data)
    
    publish_To_Topic(MQTT_Topic, sensor_json_data)
    
    print(f'Publicado fake value no canal {MQTT_Topic}')

publish_Fake_Sensor_Values_to_MQTT()

