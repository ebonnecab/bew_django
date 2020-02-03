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
        name = models.CharField(max_length=200)
        toppings = models.ManyToManyField(Topping)
        time_of_creation = models.DateField(blank=True, null=True)

        def __str__(self):
            return self.name

    ```

    8. A one-to-one relationship describes a unique connection between model A and model B. We use when it corresponds to one specific record in another table. For example, each individual only has one biological mother and one biological father.

    9. ```
        from music.models import Artist
        ```
    10. Meta class is an inner class for anything that is not a field. You use it to translate info about how the model behaves to the framework. 

    11. An example of a model method is __str__() which we use to return a string representation of an object. For an album we may want to return the full name of the album or even set a specific url for that album using get_absolute_url().

    12. An example of model inheritance is the relationship between a place and a restaurant. A restaurant is a model all on it's own but inherits the attributes of the place model as well. This is a good way of creating modular code and predefining the general attributes needed for each child model.