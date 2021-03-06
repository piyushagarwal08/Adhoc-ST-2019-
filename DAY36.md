# Django

## Notes:
* To install Django in system run
    ```
    pip3 install django
    ```
* Every time you start some project, create a new folder and 
    * run command
    ```
    django-admin startproject project-name
    ```
    * This will create a folder with the specified project-name containing all required files

* to start django server , run command
    ```
    python3 manage.py runserver
    ```
* the django framework works on 
    ```
    localhost:8000
    ```
    
## Starting with a webapp
Webapp refers to a part of your website. In Django the webiste is divide into various applications with each application having its own work.
* to create a webapp, run command
    ```
    python3 manage.py startapp app-name
    ```
* the webpages are routed as functions inside ```views.py```   
Example
    ```Python
    from django.http import HttpResponse

    def index(request):
        return HttpResponse("<h1>Text-Message</h1>")
        # HttpResponse is used like a print function to print something on web page
        # request is used to get the webpage 
    ```
    
* Every app in a project contains a file called ```urls.py``` which contains all the links related to that specific project

* in urls.py insert code as 
    ```py
    from django.urls import path
    from . import views

    urlpatterns = [
        path("",views.index,name="index"),
        path("/app1",views.func2,name="func2")
    ]
    # "" empty string denotes localhost:8000 
    ```
    
## Using Templates
### MADE SURE ALL FILES ARE PROVIDED EXECUTABLE PERMISSIONS , TO BE PRECISE 755
* In Django, to use html pages, templates are used
* Inside your webapp, create a new folder called templates and inside it make another folder with webapp name
```shell
$ mkdir -p templates/web-app
```
* Save all the html files inside this folder
* Then open, ```settings.py``` file from main project folder
* add entry 
```py
TEMPLATES = [
    {
        'DIRS': ["app-name/templates",],
    }
]
```
* To open some html webpage(template) ,In ```views.py``` file write
    
    ```python
    from django.shortcuts import render

    def index(request):
        return render(request,"app-name/page-name-stored-in-templates-dir.html")
    # render works to route the url to indicated web-page
    ```
* By Default, Django search for the folder specified in the settings.py file for templates
* To route to a different web-page using anchor-tag,the syntax is
```html
<a href="% url 'name-of-url-from-urls.py' %">text-to-work-as-link</a>
<!-- {% something %} is a format of 'jinja' language -->
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

## Using CSS,JS,BootStrap
### MADE SURE ALL FILES ARE PROVIDED EXECUTABLE PERMISSIONS , TO BE PRECISE 755
* All CSS,JS and BootStrap.. these are static files which have no need to be changes thus In Django,these are known as ```static files```
* All static files are stored inside the app in a directory named ```static``` same as templates.
* So for all img,css,js and bootstrap,create two directories
inside web-app folder
```shell
mkdir -p static/web-app/
```
* In ```settings.py``` file of main folder add a new entry in the list of ```INSTALLED_APPS```
```python
INSTALLED_APPS = [
    'web-app.apps.webappConfig',
]
```
* Finally inside your html file, do the following changes
    1. code should be initiated with following ```jinja``` code
    ```html
    {% load static %}
    ```
    2. Replace the html ```src``` tags syntax in this way
    ```html
    <img src="folder1/img/img1.jpeg"> to 
    <img src="{% static 'web-app/img/img1.jpeg' %}">

    <!-- Similarly -->
      <link href="lib/owlcarousel/assets/owl.carousel.min.css" rel="stylesheet">
                            to

    <link href="{% static 'QuizMania/lib/owlcarousel/assets/owl.carousel.min.css' %}" rel="stylesheet"> 
    ```
* {% static %} -> it tells to load the nearest static folder inside html code
* {% static 'path' %} -> is used to define the path inside of static folder for the specific file

## Routing From One Page to another (anchor)
* <b>Onclick ~ button function(using js)</b>
    1. to make a certain line of text clickable, run code in this similar context
        ```html
        <div class="col-md-6 col-lg-3">
          <div class="feature-block">
		  <img src="{% static 'QuizMania/img/docker.svg' %}" alt="img" class="img-fluid">
            <h4>Docker</h4>
            <p onclick="Docker()">Docker is a set of coupled software-as-a-service and platform-as-a-service products that use operating-system-level virtualization to develop and deliver software in packages called containers. The software that hosts the containers is called Docker Engine. </p>
          </div>
        </div>
        ```
        ```js
        <script>
            function Docker(){
                location.replace("{% url 'test' %}")
            }
        </script>
        ```
    2. <u>```onclick="function-name()"```</u> is used to point to the js code in ```script``` tag.
    3. <u> ```location.replace``` </u> is used to replace the context of current page with another with replacing chance to go back to previous page
    4. <u>```{% url 'name-of-url-in-urls.py' %}```</u> -> used to point to the different url to send on clicking the text
* After the above code , in ```html``` file, add the following lines in ```urls.py``` file pf web-app
    ```python
    from django.urls import path
    from . import views
    urlpatterns = [
        path("",views.index),
        path("any-text-to-show-after-/",views.function-name-to-change-page,name="name-for-this-url"),
        ]
    ```
* Make a new function in ```views.py``` that will do the work to render from current page to another
    ```python
    def function-name(request):
    return render(request,'web-app/page-to-load.html')
    ```
* <b> OR instead of above code,just do the following </b>
    1. in the input tag, write
    ```html
    <p onclick="window.location.href='http://localhost/2'" >any-text</p>
    ```
    2. the text will move to different url on click

## Using Loops in Templates
* for loop can be implied in a template easily using ```jinja``` format
* remember that , jinja by default thinks of ```range(value)``` as string only
* its syntax is like 
```html
<ul>
{% for test in '123' %}
    <li>hello</li>
{% endfor %}
</ul>
```
* the above code will print ```hello``` as list item 3 times
* the variable test can be accessed as ```{{test}}```


# Database
### MADE SURE ALL FILES ARE PROVIDED EXECUTABLE PERMISSIONS , TO BE PRECISE 755
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


# Users Authentication
* Create a new app called authentication

## Urls.py
* it contains 3 urls:
    1. index page
    2. login page
    3. logout page

## Views.py
* for session authentication of user at index page
    ```python
    from django.shortcuts import render

    def index(request):
        if not request.user.authenticated:
            return render(request,"users/login.html",{"message":None})
        context = {
            "user":request.user
        }
        return render(request,"users/user.html",context)
    ```        
* for login authentication, if users entered credentials are right or not,
    ```python
    from django.contrib.auth import authenticate,login
    from django.http import HttpResponseRedirect
    from django.shortcuts import render

    def login_check(request):
        username = request.POST["username-field-name"]
        password = request.POST["password-field-name"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user) # it is predefined django function to set the cookies
            return HttpResponseRedirect(reverse("index-page-name-in-urls.py"))
        else:
            return render(request,"users/login.html",{"message":'Invalid Credentials'})
    ```
* for logout , to make sure session is removed for current user, the following code is useful
    ```python
    from django.contrib.auth import logout
    from django.shortcuts import render

    def logout_check(request):
        logout(request,user)
        return render(request,"users/login.html",{"message":"Logged Out Successfully"})

## To add Users in your system Database
* Ways to be able to add users
    1. way is through Django interface shell manually
    ```python
    from django.contrib.auth.models import User

    user = User.objects.create_user("name-of-user","email-of-user","password-of-user")

    user.save()
    user.commit()
    ```
    2. we can create a registeration page and in backend run the program to insert data inside the database

* User object has various other field , that can be used to store data inside user dataabse,such as:
    1. first_name
    2. last_name
    3. administrator or not
    4. username etc
* To user modification properties of ```User``` model,just follow the similar syntax
    ```python
    from django.contrib.auth.models import User

    user = User.objects.create_user("name","email","pass")
    user.first_name = "set-any-first-name"
    user.save()
    user.save()
    ```
    
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

    
