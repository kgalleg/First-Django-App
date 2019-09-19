from django.db import models
from .library import Library
from .librarian import Librarian

#this class inherits from Model class
class Book(models.Model):

    title = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year_published = models.IntegerField()
    location = models.ForeignKey(Library, on_delete=models.CASCADE)
    #on delete --- you don't have a library you can have a book
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)
    #one to many relationship
