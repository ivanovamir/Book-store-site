from . import views
from django.urls import URLPattern, path

urlpatterns = [
    path('', views.index, name='book'),
    path('<int:pk>/', views.show_book, name='show_book'),
    path("<int:pk>/review/", views.review, name="book-review"),
    path ('category/<int:cat_id>', views.show_category, name='category'),
]

