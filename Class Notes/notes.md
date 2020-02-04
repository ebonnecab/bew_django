# Class Notes for Django

## Models
- Single definitive source of truth about data
- Usually maps to a single databse

- **Field** 
    - A class attribute that maps to a database column
    - **Types**
        - Depends on what type of data you are storing
        - There are a bunch fo different types for different use cases

    *Example of Model and Database Table*
    ```
    from django.db import models
    class Person(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)

    CREATE TABLE myapp_person (
        "id" serial NOT NULL PRIMARY KEY,
        "first_name" varchar(30) NOT NULL,
        "last_name" varchar(30) NOT NULL
        );
    ```

- command for creating a project
    - django-admin startproject "project name"
- command for creating a new app within the project
    - python3 manage.py startapp "app name"
- command for creating a super user
    - python3 manage.py createsuperuser
- django uses urlconfs to map urlpattern to views
- def view(response):
    return HttpResponse("Whatever the view is %s." % corresponding field)
- path('route', corresponding view, name="whatever i name it")
    
