# Online-courses-backend

## Otus Web Dev, HW7

This is basic backend for online-courses built in Django with packets:

 ##### Django Rest Framework: to serialize the Course Model. 
 ##### Django configurations: to separate Production from Development
 ##### Django-cors-headers : to talk to front-end
 ##### Djoser: to use simple User Management Tool


## Building

Use the python `pipenv tool to build locally from project folder:

```sh
$ pipenv shell
$ pipenv install --dev

```

## Run and View 

SQLite DB is used for the project. To run the project in Dev Environment:
```bash
$ python3 /<absolute_path>/otus-backend/manage.py migrate
$ python3 /<absolute_path>/otus-backend/manage.py createsuperuser --username=admin --email=admin@example.com
$ python3 /<absolute_path>/otus-backend/manage.py runserver
```
To run the project in Production Environment:
```bash
$ python3 /<absolute_path>/otus-backend/manage.py runserver --settings=backend.settings --configuration=Prod
```
Visit:
 `http://127.0.0.1:8000/courses` to view the api. 
 `http://127.0.0.1:8000/admin` to see admin panel. 

