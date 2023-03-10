# django-parser

## Запуск сервиса

### Через Docker 
`docker-compose build && docker-compose up -d`

### Напрямую через Python
Для этого должна быть развернута БД PostgreSQL. Данные по БД указать в .env файле
```
cd /path/to/folder/django-parser

pip install --upgrade pip
pip install -r requirements.txt

cd parser
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

python manage.py runserver
```

## Использование сервиса
Использовать сервис можно как через консоль (при помощи утилиты curl), так и через встроенный web-интерфейс по адресу http://localhost:8000/api/v1/

## Методы
Метод http://localhost:8000/api/v1/file/ позволяет загружать файлы и обрабатывать их (парсить)  
Доступны методы GET, POST


Метод http://localhost:8000/api/v1/filestotal/ позволяет посчитать тоталы по загруженным файлам  
Доступен метод GET

Параметры:
- file - фильтрация по id файла
- file__name - фильтрация по заданному имени файла на сервисе

Метод http://localhost:8000/api/v1/filesdata/ позволяет получить информацию по данным файлов  
Доступен метод GET

Параметры:
- file - фильтрация по id файла
- file__name - фильтрация по заданному имени файла на сервисе
