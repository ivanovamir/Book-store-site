from . import views
from django.urls import URLPattern, path

urlpatterns = [
    path('book/', views.BookListView.as_view(), name='book'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='show_book'),
    path("book/<int:pk>/review/", views.review, name="book-review"),
]

