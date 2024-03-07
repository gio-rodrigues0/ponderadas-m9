# Ponderada 4

Nesta ponderada, implementamos a integração do publisher feito anteriormente com um cluster no HiveMQ.

Significando que agora nos comunicamos com um broker que está na nuvem e não mais localmente, como anteriormente.

## Como utilizar

1. Primeiramente, siga todas as dependências realizadas na atividade anterior, antes da inicialização do broker.

2. Garanta que as credenciais dentro do arquivo .env estão corretas com o broker.

3. Para publicar, execute:

```sh
python3 publisher.py
```

6. Se deseja acompanhar a publicação sendo feita por meio de um subscriber, utilize:

```sh
 mosquitto_sub -h {ID_DO_CLUSTER}.s1.eu.hivemq.cloud -p 8883 -u {USUARIO} -P {SENHA} -t my/test/topic
```

## Demonstração

[Demonstração](<Screencast from 06-03-2024 23:07:32.webm>)