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
- def view(request, id):
    return HttpResponse("Whatever the view is %s." % corresponding field)
- path('route', corresponding view, name="whatever i name it")

- Model migrations copy over the changes I make to the model into the database schema.
    - python3 manage.py make_migrations
    - python3 manage.py migrate

- the through model keeps track of data about the relationship between the many to many models
    
```
Employee
    - name => CharField
    - str function return name
    - job skills => Charfield or Textfield?

Company
    - employees - manytomany field
    - name => Charfield
    - str function to return name

Work Experience
    - person -> Foreignkey
    - company -> Foreign
    - Description of role => Charfield
    - time spent at company 

Work Experience
```

```
from django.shortcuts import render, get_object
from django.views.generic.detail import DetailView

class SongDetailView(DetailView):

    model = Song

path('song/<int:pk>', views.SongDetailView.as_view(), name='song-detail')
    
```
What is a form and how do they work?
- Where do we send the data?
- Which method do we use to send the data?
    - use post to change the state of the system
        - i.e a request that saves data to db
    - use get for requests that do not affect the state of the system
        - i.e searching or filtering
- a form is a collection of elements inside of the form tag that takes input from the user and stores it in the database with a post request. It also usually has a submit button that tells the browser to send the data to the server