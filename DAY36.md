# Django

## Notes:
    * To install Django in system run
    ```
    pip3 install django
    ```
    * Every time you start some project 
        1. make a new folder and change directory
        2. run command
        ```
        django-admin startproject project-name
        ```
    * to start django server , run command
    ```
    python3 manage.py runserver
    ```
    * the django framework works on 
    ```
    localhost:8000
    ```
    
## Starting with a webapp
    *     * to create a webapp, run command
    ```
    python3 manage.py startapp app-name
    ```
    * after creating any app, open settings.py and add the name of your app in ```INSTALLED_APPS``` list
    * the webpages are made as functions inside ```views.py```
    Example
    ```python3
    from django.shortcuts import render
    from django.http import HttpResponse

    def index(request):
        return HttpResponse("<h1>Text-Message</h1>")
    ```
    * create a ```urls.py``` file to manage all the urls inside the webapp
    * in urls.py insert code as 
    ```python3
    from django.urls import path
    from . import views

    urlpatterns = [
        path("",views.index,name="index"),
    ]
    ```
    * Now restart the server 
    


    
