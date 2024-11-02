# wallet

Приложение для операций с виртуальным кошельком.

## Как развернуть проект на локальной машине.

Клонировать репозиторий и перейти в него в командной строке: 

`git clone git@github.com:Paradaise1/wallet.git`

`cd wallet`

Cоздать и активировать виртуальное окружение:

`python -m venv venv`

`source venv/Scripts/activate`

Создать и установить зависимости из файла requirements.txt: 

`python -m pip install --upgrade pip`
`pip freeze > requirements.txt`
`pip install -r requirements.txt`

Запустить docker-compose: 

`docker compose up --build`
*Может запуститься не с первого раза, тогда нужно просто переподнять докер:*
`docker compose down`
`docker compose up --build`

Теперь по адресу `http://127.0.0.1:8000/` будут доступны следующие эндпоинты:

GET /api/v1/wallets/ — получить все кошельки.
POST /api/v1/wallets/ — добавить новый кошелек.
GET /api/v1/wallets/<wallet_UUID>/ — получить конкретный кошелек по его UUID.
POST /api/v1/wallets/<wallet_UUID>/operation — изменить кошелек (положить деньги, снять деньги).

GET /docs - Swagger UI


## Примеры запросов и ответов:

*Добавить новый кошелек:*
**POST**```/api/v1/wallets/```
```
{
    "balance": "int"
}
```
Ответ:
```
{
    "id": "str"
    "balance": "int"
}
```

*изменить кошелек:*
**POST**```/api/v1/wallets/<wallet_UUID>/operation```
```
{
    "operation_type": "string",
    "amount": "int"
}
```
Ответ:
```
{
    "id": "str"
    "balance": "int"
}
```
