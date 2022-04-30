from django.contrib import admin

# Register your models here.

from .models import Book, Category, Review

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pageCount', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'pageCount')

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Category)