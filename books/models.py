from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50, null=True)
    pageCount = models.IntegerField(null=True)
    description = models.TextField(null=True)
    photo = models.ImageField(null=True, upload_to = "images/%Y/%m/%d/", default='books/default_book.png')
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title}, {self.pageCount}"

    def get_absolute_url(self):
        return reverse ('show_book', kwargs ={'pk': self.pk})

class Review(models.Model):
    book_id = models.IntegerField()
    body = models.TextField()
    post_time_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse ('book-review', kwargs ={'pk': self.book_id})

class Category(models.Model):
    name = models.CharField(max_length = 50, db_index=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse ('category', kwargs ={'cat_id': self.pk})