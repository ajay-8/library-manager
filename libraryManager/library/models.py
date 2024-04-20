from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author, related_name='authors_book')
    isbn = models.CharField(max_length=13)
    publication_date = models.DateField()
    genre = models.CharField(max_length=100)
    quantity_in_stock = models.PositiveIntegerField()

    def __str__(self):
        return self.title


