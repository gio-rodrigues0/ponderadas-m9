# Ponderada 1

Nesta ponderada, implementamos um publisher responsável por enviar dados de um sensor simulado. O sensor simulado é um script gerador de valores aleatórios.

## Gerador

Para criar os dados simulados, é necessário fornecer a quantidade de dados, o valor mínimo e o valor máximo como argumentos ao executar o script. A função então utiliza esses valores como parâmetros e os salva em um arquivo CSV.

## Publisher

No publisher, o primeiro passo é a configuração, onde os dados contidos em um arquivo JSON de configuração são lidos e salvos em um objeto. Em seguida, cada linha do arquivo CSV de dados é lida. Para cada linha, um JSON é criado, combinando o valor do CSV com as informações recebidas no JSON de configuração, como tipo de sensor e localização. Esses valores são então publicados, seguindo a frequência especificada no arquivo JSON de configuração.

## Como utilizar

1. Primeiramente, instale as dependências necessárias:

```sh
pip install csv
```

```sh
sudo apt-get install mosquitto mosquitto-clients
```

2. Crie o arquivo de configuração do broker, chamado `mosquitto.conf`:

```
listener 1891
allow_anonymous true
```

3. Inicie o broker localmente:

```sh
mosquitto -c mosquitto.conf
```

4. Para gerar os valores do sensor, execute o seguinte comando:

```sh
python3 gerador.py <quantidade_de_dados> <valor_mínimo> <valor_máximo>
```

5. Para publicar, execute:

```sh
python3 publisher.py
```

6. Se desejar alterar as configurações do sensor, acesse o arquivo `config.json` e edite as informações conforme sua preferência.

## Demonstração

[Demonstração](<Screencast from 18-02-2024 23:36:26.webm>)