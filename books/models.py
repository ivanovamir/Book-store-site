from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField
from django.urls import reverse

class Book(models.Model):
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50, null=True)
    pageCount = models.IntegerField(null=True)
    description = models.TextField(null=True)
    photo = models.ImageField(null=True, upload_to = "books/%Y/%m/%d/", default='books/default_book.png')
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}, {self.pageCount}"

    def get_absolute_url(self):
        return reverse ('show_book', kwargs ={'slug_book': self.slug})

    class Meta:
        verbose_name = 'list of books'
        # verbose_name_plural = 
        ordering = ['title', 'id']



class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    body = models.TextField(max_length=250)
    post_time_created = models.DateTimeField(auto_now_add=True, null=True)

    def total_comments(self):
        return self.id.count()

    def __str__(self):
        return self.id

    def get_absolute_url(self): 
        return reverse ('book-review', kwargs ={'pk': self.book})

    class Meta:
        verbose_name = 'list of reviews'
        ordering = ['post_time_created']


class Category(models.Model):
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')
    name = models.CharField(max_length = 50, db_index=True)
    photo = models.ImageField(null=True, upload_to = "books/%Y/%m/%d/", default='books/default_book.png')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse ('category', kwargs ={'slug_id': self.slug})

    class Meta:
        verbose_name = 'list of categories'
        ordering = ['id']
