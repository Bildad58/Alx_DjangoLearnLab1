from django.db import models

<<<<<<< HEAD
=======
from django.db import models
>>>>>>> 74694a0488bb0d3ed45ebf4b3e39cf5ad900e511

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField

    def __str__(self):
        return self.title
<<<<<<< HEAD

=======
# Create your models here.
# Create your models here.
>>>>>>> 74694a0488bb0d3ed45ebf4b3e39cf5ad900e511
