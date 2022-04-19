from django.shortcuts import render, redirect
# from numpy import generic
from .models import Book, Review
# from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.views.generic import ListView, DetailView


class BookListView(ListView):
    template_name = 'books/home.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()

# def index(request):
#     dbData = Book.objects.all()
#     context = {'books' : dbData}
#     return render (request, 'books/home.html', context)

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/show_book.html'
    

# def show_book(request, pk):
#     single_book = get_object_or_404(Book,pk=pk)
#     reviews = Review.objects.filter(book_id=pk).all()
#     context = {'book' : single_book, 'reviews':reviews}
#     return render (request, 'books/show_book.html', context)

def review(request, pk): 
    review_body = request.POST['review']
    review = Review(body=review_body, book_id=pk)
    review.save()
    return redirect('/book')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Sorry</h1>')
    