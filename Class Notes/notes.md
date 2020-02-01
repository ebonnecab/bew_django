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
    
