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
* to create a webapp, run command
    ```
    python3 manage.py startapp app-name
    ```
* after creating any app, open settings.py and add the name of your app in ```INSTALLED_APPS``` list
* the webpages are made as functions inside ```views.py``` 
Example
    ```Python
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
    
* To open some webpage (html),In ```views.py``` file write
    ```python
    from django.shortcuts import render

    def index(request):
        return render(request,"app-name/page-name-stored-in-templates-dir.html")
    
    ```
* save the html page in new folder ```templates/app-name/```
* To route to a different web-page using anchor-tag,the syntax is
```html
<a href="% url 'name-of-url-from-urls.py' %">text-to-work-as-link</a>
```
* For similar structured web-pages,instead of repeating the html code
    1. create a base.html file with the html structure code
    ```html
    <!DOCTYPE html>
    <html>
        <head>
            <title>{% block title %}{% endblock %}</title>
        </head>
        <body>
            {% block body %}
            {% endblock %}
        </body>
    </html>
    ```
    2. For all other files, the code will be similar to
    ```html
    {% extends "path-of-base.html" %}

    {% block title %}
        Title-of-your-page
    {% endblock %}
    
    {% block body %}
        <h1> this is my body content </h1>
    {% endblock %}
    ```



# Database
* To create a superuser to access all the tables inside a database,run command
    ```python
     python manage.py createsuperuser
    ```
* The tables and databases are creates in ```models.py``` file
* ```context``` keyword is used to create a dictionary inside a function of ```views.py``` which can be accessed as a variable
Example
```python
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        "key-name": database-class-name.objects.all()
    }
    return render(request,"html-page-to-take-the-data-to-from-database",context)
```
## Create New Table
* To create any kind of table ,just
    1. open models.py
    2. write in the following pattern
    ```python
    from django.db import models

    class table-name(models.Model):
        column1-name = models.CharField(max_length=45)
        column2-name = models.IntegerField(max_length=10)

        # the way to represent the data when called
        def __str__(self):
            return f"{self.column1-name} its just a string {self.column2-name} "
    ```
    3. to commit changes in database , run command
    it will create a table and output a id
    ```
    python manage.py makemigrations
    ```
    4. To check the actual SQL query would have needed to do the upper task , run command 
    ```
    python manage.py sqlmigrate project-name table-id
    ```
    5. To finally apply all the changes , run command
    ```
    python manage.py migrate
    ```
## Table Relationships
* To define relationships between different tables, django supports various formats such as :
    1. ForeignKey(table-name,on_delete=models.CASCADE,related_name="")
    2. ManyToMany(table-name,on_delete=models.CASCADE,related_name="")
* <u>on_delete function</u>: it is used to delete an entry automatically if its deleted from linked table
* <u>related_name</u>: it is used to refer the column and access its content with ```.```

## Admin-Database Configuration
*  file ```admin.py``` contains list of all the tables made inside a project
* the file looks like,
    ```python
    from django.contrib import admin
    from .models import Table-name1, Table-name2
    # register models name
    admin.site.register(Table-name1)
    admin.site.register(Table-name2)
    ```
## Data Extraction from forms
* its very simple to extract data from some page that is by:
    ```python

    variable-name = request.POST['name-of-input-field']
    ```
* To redirect user to any other page
    ```python
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    def redirect_function(request):
        return HttpResponseRedirect(reverse("name-of-url",args=None/if-any))
    ```
* to show 404 error page
    ```python
    from django.http import Http404
    try:
        # some statements
    except:
        raise Http404("Statement to show as error")
    ```
* while making forms always make sure to add ```{% csrf_token %}``` tag inside the form
* <u>csrf_token</u> : By default, for security reasons , django doesn't support submission of forms and thus requires this token to know that actually our web  application is submitting this form 



# HTML

## Attributes
<b>ID </b>
* it can be used to make a particular id for a specific tag such it can be referred to later easily
    * example
        ```html
        <h1 id="section1">Hello</h1>
        <h2 id="chutiya" > World</h2>
        < a href="#section1">link</a>
        ```
* on clicking link, it will scroll the page to h1 tag

    
