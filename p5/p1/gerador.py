import csv
import random
import sys

def gerar_dado(minimo, maximo):
    dado = random.uniform(minimo, maximo)
    return dado

def escrever_csv(quantidade):
    with open('dados.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(quantidade):
            dado = gerar_dado(minimo, maximo)
            writer.writerow([dado])

quantidade = int(sys.argv[1])
minimo = float(sys.argv[2])
maximo= float(sys.argv[3])

print(f"Gerando {quantidade} dados entre {minimo} e {maximo}")

escrever_csv(quantidade)