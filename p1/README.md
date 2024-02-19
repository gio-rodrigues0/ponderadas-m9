# Ponderada 1

Nessa ponderada, foi implementado um publisher que envia dados de um sensor simulado, sendo esse, um script gerador de valores aleatórios.

## Gerador

Na criação dos dados simulados, é preciso passar a quantidade de dados, o valor mínimo e máximo como argumentos ao executar o script. Assim, a função usa esses valores como parametros e os salva num csv.

## Publisher

No publisher, temos primeiro a etapa de configuração, onde os dados encontrados dentro de um json de configuração serão lidos e salvos num objeto. Depois, temos a leitura de cada linha do nosso csv de dados, a cada linha, um json é criado, unindo o valor do csv com as informações recebidas no json de configuração, como tipo de sensor e localização. Então, temos a publicação desse valor, sendo cada publicação seguindo a frequencia passada no json de configuração.

## Como utilizar

1. Primeiro, instale as dependências necessárias:

´´´
pip install csv
´´´

´´´
sudo apt-get install mosquitto mosquitto-clients
´´´

2. Crie o arquivo de configuração do broker, chamando de mosquitto.conf:

´´´
listener 1891
allow_anonymous true
´´´

3. Inicie o broker localmente:

´´´
mosquitto -c mosquitto.conf
´´´

4. Para gerar os valores do sensor, rode o seguinte comando:

´´´
python3 gerador.py <quantidade_de_dados> <valor_mínimo> <valor_máximo>
´´´

5. Para publicar, rode:

´´´
python3 publisher.py
´´´

6. Caso queira mudar as configurações do sensor, acesse o arquivo config.json e troque as informações a sua preferência.

## Demonstração

[Demonstração](<Screencast from 18-02-2024 23:36:26.webm>)