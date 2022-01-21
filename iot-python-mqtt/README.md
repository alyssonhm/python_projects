# Python MQTT IOT

Exemplo de um projeto simples de [IOT](https://www.redhat.com/pt-br/topics/internet-of-things/what-is-iot), usando o protocolo MQTT, HiveMQ Cloud como broker, Eclipse Paho Python Client e banco de dados SQLite.


Basicamento ele conecta os clients MQTT no broker do HiveMQ Cloud, enviando e recebendo mensagens usando o protocolo MQTT e gravando os dados no SQLite.

* Link para documentação da biblioteca Eclipse Paho [AQUI](https://www.hivemq.com/blog/mqtt-client-library-paho-python/)
* Link para o site HiveMQ Cloud Broker [AQUI](https://www.hivemq.com/mqtt-cloud-broker/)
* Um pouco sobre o protocolo MQTT [AQUI](https://medium.com/python-point/mqtt-basics-with-python-examples-7c758e605d4)

## Executando

**OBS**: Para executar este projeto, você precisa ter o Python instalado na versão 3.8 ou acima.

* Primeiro, instale os requisitos conforme abaixo no terminal de comandos:
```sh
pip install -r requirements.txt
```
* Ainda no terminal digite o comando abaixo para criar a base de dados e a tabela necessária:
```
python createDB.py
```
* Após isso execute o comando abaixo:
```
python mqttListener.py
```

O listener ficará executando e aguardando as mensagens serem publicadas.

## Enviando uma mensagem de teste ao listener:

* Instale um client MQTT em sua máquina, no caso, utilizei o [Eclipse Mosquitto MQTT](https://www.arubacloud.com/tutorial/how-to-install-and-secure-mosquitto-on-ubuntu-20-04.aspx)
* Depois, abra outro terminal de comandos e digite:
```
mosquitto_pub -h <broker_hostname> -p <porta> -u <usuario> -P <password> -t '<tópico>' -m '<mensagem>'
```
**OBS:** A mensagem deve ser no formato JSON:

**Ex:** {"SensorID": "sensor1","Temperatura": "35", "Umidade": "72"}