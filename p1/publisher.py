import paho.mqtt.client as mqtt
import time
import json
import csv

class Configuracao:
    def __init__(self, sensor, longitude, latitude, frequencia):
        self.sensor = sensor
        self.longitude = longitude
        self.latitude = latitude
        self.frequencia = frequencia

# Configuração do cliente
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_publisher")

# Conecte ao broker
client.connect("localhost", 1891, 60)

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
    client.publish("test/topic", message)
    print(f"Publicado: {message}")
    periodo = 1 / configuracao.frequencia
    print(f"Esperando {periodo} segundos")
    time.sleep(periodo)

configuracao = configurar()
leitura_csv()

client.disconnect()

