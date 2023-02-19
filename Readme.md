# Bookstore
___
![python_version](https://img.shields.io/badge/python-3.11-orange)
![django_version](https://img.shields.io/badge/django-4.1-orange)
![psycopg_version](https://img.shields.io/badge/psycopg2-2.9.5-orange)
![bootstrap_version](https://img.shields.io/badge/bootstrap-5-orange)
![django--allauth_version](https://img.shields.io/badge/django--allauth-0.51.0-orange)
![django--crispy--forms_version](https://img.shields.io/badge/django--crispy--forms-1.14.0-orange)
![pillow_version](https://img.shields.io/badge/pillow-9.3.0-orange)
![whitenoise_version](https://img.shields.io/badge/whitenoise-6.2.0-orange)
![gunicorn_version](https://img.shields.io/badge/gunicorn-20.1.0-orange)

В данном приложении можно регистрироваться, добавлять, редактировать и 
удалять книги, а также отзывы к ним. Реализован поиск по названию книги
или его автору. Возможен просмотр книг как списком, так и по отдельности.
![demo1](demo1.jpg)
![demo2](demo2.jpg)
![demo3](demo3.jpg)

## Настройка перед запуском

Первое, что нужно сделать, это cклонировать репозиторий:

```sh
$ git clone https://github.com/Andrei2020-web/Bookstore.git
$ cd Bookstore
```

Создайте виртуальную среду для установки зависимостей и активируйте ее:

```sh
$ virtualenv venv
$ source venv/bin/activate
```

Затем установите зависимости:

```sh
(venv)$ pip install -r requirements.txt
```

Запускаем сервер:

```sh
(venv)$ python manage.py runserver
```