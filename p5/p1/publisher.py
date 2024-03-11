import paho.mqtt.client as paho
import time
import json
import csv
import os
from dotenv import load_dotenv
from paho import mqtt
import requests

class Configuracao:
    def __init__(self, sensor, longitude, latitude, frequencia):
        self.sensor = sensor
        self.longitude = longitude
        self.latitude = latitude
        self.frequencia = frequencia

load_dotenv()

broker_address = os.getenv("BROKER_ADDR")
port = 8883
topic = "my/test/topic"
username = os.getenv("HIVE_USER")
password = os.getenv("HIVE_PSWD")

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"CONNACK received with code {reason_code}")

def on_publish(client, userdata, mid, reason_code, properties):
    print(f"Mid: {mid}")

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(f"{msg.topic} (QoS: {msg.qos}) - {msg.payload.decode('utf-8')}")

# Instanciação do cliente
client = paho.Client(paho.CallbackAPIVersion.VERSION2, "Publisher",
                     protocol=paho.MQTTv5)
client.on_connect = on_connect

# Configurações de TLS
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set(username, password)  # Configuração da autenticação

client.on_message = on_message
client.on_publish = on_publish

# Conexão ao broker
client.connect(broker_address, port=port)

# Configuração do cliente
# client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_publisher")

# Conecte ao broker
# client.connect("localhost", 1891, 60)

def criar_json(dado):
    formatacao_json = {
        "sensor": configuracao.sensor,
        "longitude": configuracao.longitude,
        "latitude": configuracao.latitude,
        "dado": dado
    }

    dado = json.dumps(formatacao_json)

    return dado

# Loop para publicar mensagens continuamente
def leitura_csv():
    with open('dados.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            dado = criar_json(row)
            publicar(dado)
    

def configurar():
    with open('config.json', 'r') as arquivo:
        leitura = json.load(arquivo)
        return Configuracao(leitura['sensor'], leitura['longitude'], leitura['latitude'], leitura['frequencia'])

def publicar(dado):
    message = dado
    client.publish(topic, payload=message, qos=1)
    requests.post('http://localhost:5000/dados', json=json.loads(dado))
    print(f"Publicado")
    periodo = 1 / configuracao.frequencia
    # print(f"Esperando {periodo} segundos")
    x = requests.get('http://localhost:5000/dados')
    print(x.text)
    time.sleep(periodo)

configuracao = configurar()
leitura_csv()

client.loop_forever()
