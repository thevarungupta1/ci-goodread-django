# Goodread - API Development Project

In this project, we will build a compete REST API for Goodread Project

## Module 01 - Setting Up Project

### Basic Project Setup

Create a virtaul environment for the Goodread Project

```bash
> python -m venv menv
> menv\Scripts\activate
> python -m pip install Django
> pip freeze
> python -m pip install --upgrade pip    // optional
```

### Installation

Setup the django project

```bash
> django-admin startproject goodread
> cd goodread
> python manage.py startapp goodread_app
> python manage.py runserver

Starting development server at http://127.0.0.1:8000/
```


## Module 02 - Models and Migrations

create migration and super user

```bash
> cd goodread

goodread/settings.py

INSTALLED_APPS = [
    ...
    'goodread_app',
]

> python manage.py migrate
> python manage.py createsuperuser
Username (leave blank to use 'admin'):
Email address:
Password:[ENTER PASSWORD]
Password (again):[ENTER PASSWORD AGAIN]
The password is too similar to the username.
This password is too common.
Bypass password validation and create user anyway? [y/N]: [y]
Superuser created successfully.

> python manage.py runserver
Starting development server at http://127.0.0.1:8000/

http://localhost:8000/admin/
```


Create our first model

```bash
goodread_app/models.py

from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

> python manage.py makemigrations
> python manage.py migrate
> python manage.py runserver

```