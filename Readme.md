### Поиск аномалий во временных рядах

#### Запуск

Склонировать репозитарий и перейти в директорию проекта:

```BASH
git clone https://github.com/mechnotech/time_series_task.git
cd time_series_task/
```

Создать и активировать виртуальное окружение python:

```BASH
python3 -m venv venv
source venv/bin/activate
```

Установить зависимости:

```BASH
pip install -r requirements.txt
```

Запустить приложение:

```BASH
python3 app.py
```
Приложение будет доступно по адресу:

http://localhost:8050


#### Запуск приложения в контейнере:

```BASH
docker-compose up --build -d
```

Приложение будет доступно по адресу:

`http://localhost:8050`