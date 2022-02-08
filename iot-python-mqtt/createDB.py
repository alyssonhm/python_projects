# ------------------------------------------
# --- Desenvolvedor.: Alysson Morandi
# --- Data..........: 21/01/2022
# --- Objetivo......: Criar o database e a tabela no sqlite
# --- Python Version: 3.8
# ------------------------------------------

import sqlite3

# Database name
DB_Name = 'mqtt.db'

# Script da tabela
TableSchema = """
drop table if exists sensors_data ;
create table sensors_data (
  id integer primary key autoincrement,
  SensorID text,
  Location text,
  DateTime text,
  Temperatura text,
  Umidade text
);
"""
#conecta na base
conn = sqlite3.connect(DB_Name)
curs = conn.cursor()

# Cria tabela
sqlite3.complete_statement(TableSchema)
curs.executescript(TableSchema)

# Fecha conexão com o database criado
curs.close()
conn.close()