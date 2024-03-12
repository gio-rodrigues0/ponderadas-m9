# Ponderada 5

Nesta ponderada, implementamos a integração do nosso publisher com uma ferramenta de Business Inteligence, o Metabase.

## Armazenamento

Para o armazenamento dos dados que alimentaram o Metabase, foi utilizado um banco de dados SQLite junto com um pequeno backend em Python.

Quando um dado é publicado no tópico, uma rota de POST é chamada e armazena o json enviado no banco.

## Como utilizar

1. Primeiro, é necessária ter Docker instalado na máquina, para então, rodarmos o arquivo docker-compose, que rodará o Metabase garantindo a persistência dos dados. Não esqueça de abrir o Docker.

```sh
docker compose up
```

```sh
sudo apt-get install mosquitto mosquitto-clients
```

2. Agora, já podemos iniciar o nosso backend, que criará a nossa tabela, se ela já não existir, e disponibilizará nossa rota.

```
python3 backend.py
```

3. Já é possível começar as publicações, verifique se o arquivo de configuração está correto e gere novos dados se quiser. Se já estiver tudo pronto, manda bala no comando:

```sh
python3 publisher.py
```

4. Para visualizá-los pelo Metabase, acesse localhost:3000.

## Demonstração

Meus vídeos não funcionam mais aqui, ainda não descobri o motivo :(