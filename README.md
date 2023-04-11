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


goodread_app/admin.py

from django.contrib import admin
from goodread_app.models import Book

# Register your models here.
admin.site.register(Book)
```


## Module 03 - Install Django REST framework

Django REST framework is a powerful and flexible toolkit for building Web APIs.

```bash
> pip install djangorestframework

goodread/settings.py

INSTALLED_APPS = [
    ...
    'goodread_app',
    'rest_framework',
]
```


## Module 04 - Create api for Book - Get

create a rest api to fetch book data (getAllBooks and getBookById)

create a new folder "api" inside goodread_app folder to have common place to have all api related code

### create file goodread_app/api/serializers.py

```bash
from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    author = serializers.CharField()
    description = serializers.CharField()
    image = serializers.CharField()
    rating = serializers.DecimalField(max_digits=5, decimal_places=2)
    active = serializers.BooleanField()
```

### create file goodread_app/api/views.py 

```bash
from rest_framework.response import Response
from rest_framework.decorators import api_view
from goodread_app.models import Book
from goodread_app.api.serializers import BookSerializer


@api_view()
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view()
def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)
```

### create file goodread_app/api/urls.py

```bash
from django.urls import path, include
from goodread_app.api.views import book_list, book_details

urlpatterns = [
    path('list/', book_list, name='book-list'),
    path('<int:pk>/', book_details, name='book-detail'),
]
```

### update file goodread/urls.py

```bash
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('goodread_app.api.urls'))
]
```

### Open the browser and test api
```bash
http://localhost:8000/book/list/
http://localhost:8000/book/1
```


## Module 05 - Create api for Book - Post, Put and Delete

Create a REST API for Book  - Post, Put and Delete

### update file goodread_app/api/serializers.py

```bash
from rest_framework import serializers
from goodread_app.models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    author = serializers.CharField()
    description = serializers.CharField()
    image = serializers.CharField()
    rating = serializers.DecimalField(max_digits=5, decimal_places=2)
    active = serializers.BooleanField()
    
    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
```

### update file goodread_app/api/views.py

```bash
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from goodread_app.models import Book
from goodread_app.api.serializers import BookSerializer


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def book_details(request, pk):
    if request.method == 'GET':
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        book = Book.objects.get(pk=pk)
        book.delete()
        # return Response(serializer.data)
        return Response(status=status.Http_204_NO_CONTENT)
```

### Open the browser and test api
```bash
http://localhost:8000/book/list/ - GET | POST
http://localhost:8000/book/1 - GET | PUT | DELETE
```