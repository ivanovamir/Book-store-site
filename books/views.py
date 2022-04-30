from django.shortcuts import render, redirect
# from numpy import generic
from .models import Book, Review, Category
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views.generic import ListView, DetailView


# class BookListView(ListView):
#     template_name = 'books/home.html'
#     context_object_name = 'books'

#     def get_queryset(self):
#         return Book.objects.all()

def index(request): #same
    dbData = Book.objects.all()
    cat = Category.objects.all()
    context = {'books' : dbData, 'cat':cat, 'cat_selected':0}
    return render (request, 'books/home.html', context)

# class BookDetailView(DetailView):
#     model = Book
#     template_name = 'books/show_book.html'
def all_category(request):
    cat = Category.objects.all()
    context = {'cat':cat}
    return render (request, 'books/all_category.html', context)

def show_category(request, cat_id): #same
    books = Book.objects.filter(cat_id=cat_id)
    cat = Category.objects.all()
    context = {'books' : books, 'cat':cat, 'cat_selected':cat_id}
    return render (request, 'books/list_book.html', context)
    

def show_book(request, pk):
    single_book = get_object_or_404(Book,pk=pk)
    reviews = Review.objects.filter(book_id=pk).all()

    ####
    
    context = {'single_book' : single_book, 'reviews':reviews}
    return render (request, 'books/show_book.html', context)

def review(request, pk): 
    review_body = request.POST['review']
    review = Review(body=review_body, book_id=pk)
    review.save()
    return redirect('book')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
    