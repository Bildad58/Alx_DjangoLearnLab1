from django.db import models

<<<<<<< HEAD
=======
from django.db import models

>>>>>>> 74694a0488bb0d3ed45ebf4b3e39cf5ad900e511
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
# Create your models here.
<<<<<<< HEAD

# Create your models here.
=======
>>>>>>> 74694a0488bb0d3ed45ebf4b3e39cf5ad900e511
