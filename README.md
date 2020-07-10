# Тестовое задание Ubex
## динамическая генерация JSON REST API ендпоинтов при создании новых моделей

### актуальное файловое дереров:
``` .
    ├── book
    │   ├── __pycache__
    │   │   ├── __init__.cpython-38.pyc
    │   │   ├── admin.cpython-38.pyc
    │   │   ├── models.cpython-38.pyc
    │   │   └── tests.cpython-38.pyc
    │   ├── migrations
    │   │   ├── __pycache__
    │   │   │   ├── 0001_initial.cpython-38.pyc
    │   │   │   ├── 0002_auto_20200709_2113.cpython-38.pyc
    │   │   │   ├── 0002_auto_20200710_1135.cpython-38.pyc
    │   │   │   ├── 0002_auto_20200710_1201.cpython-38.pyc
    │   │   │   ├── 0002_auto_20200710_1216.cpython-38.pyc
    │   │   │   ├── 0002_auto_20200710_1229.cpython-38.pyc
    │   │   │   ├── 0002_auto_20200710_1242.cpython-38.pyc
    │   │   │   ├── 0003_auto_20200709_2116.cpython-38.pyc
    │   │   │   ├── 0003_auto_20200710_1231.cpython-38.pyc
    │   │   │   ├── 0003_auto_20200710_1245.cpython-38.pyc
    │   │   │   ├── 0004_auto_20200709_2203.cpython-38.pyc
    │   │   │   ├── 0005_auto_20200709_2207.cpython-38.pyc
    │   │   │   └── __init__.cpython-38.pyc
    │   │   ├── 0001_initial.py
    │   │   └── __init__.py
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── dynamic_models_viewset
    │   ├── __pycache__
    │   │   ├── __init__.cpython-38.pyc
    │   │   ├── settings.cpython-38.pyc
    │   │   ├── urls.cpython-38.pyc
    │   │   └── wsgi.cpython-38.pyc
    │   ├── settings
    │   │   ├── __pycache__
    │   │   │   ├── __init__.cpython-38.pyc
    │   │   │   ├── base.cpython-38.pyc
    │   │   │   ├── rest.cpython-38.pyc
    │   │   │   └── settings.cpython-38.pyc
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   └── rest.py
    │   ├── __init__.py
    │   ├── db.sqlite3
    │   ├── urls.py
    │   └── wsgi.py
    ├── generic_apiview
    │   ├── __pycache__
    │   │   ├── __init__.cpython-38.pyc
    │   │   ├── admin.cpython-38.pyc
    │   │   ├── models.cpython-38.pyc
    │   │   ├── tests.cpython-38.pyc
    │   │   ├── urls.cpython-38.pyc
    │   │   ├── utils.cpython-38.pyc
    │   │   └── views.cpython-38.pyc
    │   ├── migrations
    │   │   ├── __pycache__
    │   │   │   └── __init__.cpython-38.pyc
    │   │   └── __init__.py
    │   ├── serializers
    │   │   ├── __pycache__
    │   │   │   ├── __init__.cpython-38.pyc
    │   │   │   └── main_serializer.cpython-38.pyc
    │   │   ├── __init__.py
    │   │   └── main_serializer.py
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── utils.py
    │   └── views.py
    ├── manage.py
    ├── pytest.ini
    └── tree.sh
```

#### **generic_apiview** - расширение автоматического  REST API
#### **book** - условное приложение с полями данных

## Usage:
подключение:
	* установить generic_apiview в INSTALLED_APPS
	* указать в моделях данных models.Model аттрибут serialize_fields перечислящий поля для сериализации
	'''
	    ...
		serialize_fields = [
			'id', 'title', 'description', 'authors'
		]
		...
	
	'''

#### все эндпоинты будут даступны по аддресу: ...:8000/api/.... прим. (http://0.0.0.0:8000/api/book)



# API методы и аргументы:

#### 1) GET http://0.0.0.0:8000/api/book
##### в случае отсутсвия аргументов вернет отсортированный по убыванию id массив длинной 20 объектов.
##### ожидаемые параметры: 
**order_by** - принимает любые значение поддающиеся сортировке (время, числа и id). Порядок по убыванию указывается через через "-date"
**limit** - по умолчанию установлено 20 записей.
##### возможно употребление раззнообразных аргументов в соответствии с логикой запросов ORM  Django

#### 2) POST http://0.0.0.0:8000/api/book 
##### создаёт запись книги в базе данных, в качестве аргументов принимает любоей кол-во созданных в модели данных и полученных
##### при вызове GET метода. Логика обязательных и необязаттельных полей описывается вне расширения.

#### 3) PUT http://0.0.0.0:8000/api/book/1
##### позволяет обновить объект книги с id 1. В качестве аргументов принимает любые параметры полученный в ответ от сервера.

#### 4) DELETE  http://0.0.0.0:8000/api/book/1
##### удаляет объект книги с id 1


#### для запуска тестов:
* создание объектов
'''shell
python manage.py test generic_apiview.tests.GetTest.setUp
'''
* проверка целостности
'''shell
python manage.py test generic_apiview.tests.GetTest.test_get_all_book
'''

* проверка записи
'''shell
python manage.py test generic_apiview.tests.GetTest.post
'''
* обновление
'''shell
curl  -X PUT -H "Content-Type: application/json" -d '{"title":"","description":"отредактированное "}'  http://localhost:8000/api/book/1
'''

* удаление
'''shell
curl -X DELETE  http://localhost:8000/api/book/1 
'''