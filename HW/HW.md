1. A field represents the attributes associated with the model. The field type depends what kind of data you want to store and what is best for your use case. For example, a TextField is better for large amounts of text than a CharField but they both take string inputs.

2. Null determines whether a database column will accept null values. Blank determines whether an input is required for that field to be valid. One is on the database level, one is on the application level.

3. TextChoices are a more concise way of defining the choices for a given field within a subclass that can be easily enumerated over.

4. The primary key is a unique identifier for every object or column in the table.

5. A verbose name is a parameter inside of every field where you explicity state what the user will input for that form. It's purpose is to cut out ambiguity and/or hide the default name from the database table.

6. ```
    class Manufacturer(models.Model):
        name = models.CharField(max_length=200)
        def __str__(self):
            return self.name

    class Car(models.Model):
        manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
        name = models.CharField(max_length=200)
        manafacture_date = models.DateField(blank=True, null=True)
        def __str__(self):
            return self.name
    ```

7. ```
    from django.db import models

    class Topping(models.Model):
        name = models.CharField(max_length=200)
        def __str__(self):
            return self.name

    class Pizza(models.Model):
       
        toppings = models.ManyToManyField(Topping)

    ```