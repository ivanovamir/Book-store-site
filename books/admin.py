from django.contrib import admin

# Register your models here.

from .models import Book, Category, Review

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Category)