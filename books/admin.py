from django.contrib import admin
from .models import *

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pageCount', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'pageCount')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name')
    prepopulated_fields = {"slug":("name",)}

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Category)