from django.contrib import admin

# Register your models here.

from .models import Book, Review

admin.site.register(Book)
admin.site.register(Review)