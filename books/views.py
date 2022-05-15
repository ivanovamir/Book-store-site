from pdb import post_mortem
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Review, Category
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .forms import *

class Home(ListView):
    model = Book
    template_name = 'books/home.html'

# def index(request): #main page
#     dbData = Book.objects.all()
#     context = {'books' : dbData, 'cat_selected':0}
#     return render (request, 'books/home.html', context)


def all_category(request):
    return render (request, 'books/all_category.html')

def show_category(request, slug_id):
    cat_name = Category.objects.get(slug=slug_id)
    books = Book.objects.filter(cat_id=cat_name)
    # for book in books:
    #     if book.pageCount <= 200:
    #         book_1 = book
    #     elif book.pageCount>=201 and book.pageCount<=500:
    #         book_2 = book
    #     else:
    #         book_3 = book
    context = {'books' : books, 'cat_name':cat_name}
    return render (request, 'books/list_book.html', context)
    

def show_book(request, slug_book):
    single_book = get_object_or_404(Book,slug=slug_book)
    reviews = Review.objects.filter(book=single_book)

    ####
    
    context = {
        'single_book' : single_book,
        'reviews':reviews,
        }
    return render (request, 'books/show_book.html', context)

def review(request, slug_book):
    book = Book.objects.get(slug=slug_book)
    review_body = request.POST['review']
    review = Review(body=review_body, book=book)
    review.save()
    return redirect ('book')
    


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
    