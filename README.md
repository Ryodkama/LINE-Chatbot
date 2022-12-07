# LINE-Chatbot

### How to use

- docker の立ち上げ

```
docker-compose up -d
docker-compose up -d --build
```

- docker の中に入る

```
docker-compose exec server bash
```

- chatbot に移動し以下コマンドを実行

```
python manage.py runserver 0.0.0.0:8000
```

## migrations

- migrations ファイルを削除

- migrations を行う

```
python manage.py makemigrations
```

- migrations を適用

```
python manage.py migrate
```
