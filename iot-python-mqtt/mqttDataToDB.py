# ------------------------------------------
# --- Desenvolvedor.: Alysson Morandi
# --- Data..........: 21/01/2022
# --- Objetivo......: Grava na base de dados (SQLite) os dados recebidos no tópico MQTT
# --- Python Version: 3.8
# ------------------------------------------

from asyncio.log import logger
import json
import sqlite3
from datetime import datetime

# Database Name
DB_Name = 'mqtt.db'

# definição de classe para manipular dados no sqlite
class Database:

    def __init__(self):
        self.conn = sqlite3.connect(DB_Name)
        self.conn.commit()
        self.cur = self.conn.cursor()

    def manipula_dados(self, sql_query, args=()):
        try:
            self.cur.execute(sql_query, args)
            self.conn.commit()
            print('Valores inseridos na tabela.')
            print('')
            return
        except sqlite3.Error as err:
            print(f'Erro no database: {err}')
            self.conn.close()
            return

    def __del__(self):
        self.cur.close()
        self.conn.close()


# Função para manipular o JSON enviado pelo MQTT e gravar os dados na base sqlite
def sensor_data(jsondata):
    # Parse JSON
    json_dict = json.loads(jsondata)
    sensor_id = json_dict['SensorID']
    location = json_dict['Location']
    date_time = (datetime.now()).strftime('%d/%m/%Y %H:%M:%S') # pega a data e hora atual dd/mm/YY H:M:S   
    temperatura = json_dict['Temperatura']
    umidade = json_dict['Umidade']

    # Instancia a classe e grava na tabela
    database = Database()
    database.manipula_dados(
        'insert into sensors_data (SensorID, Location, DateTime, Temperatura, Umidade) values (?,?,?,?,?)',
        [sensor_id, location, date_time, temperatura, umidade])
    del database
