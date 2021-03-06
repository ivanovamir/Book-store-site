from . import views
from django.urls import URLPattern, path

urlpatterns = [
    path('', views.Home.as_view(), name='book'),
    path('<slug:slug_book>/', views.show_book, name='show_book'),
    path("<slug:slug_book>/review/", views.review, name="book-review"),
    path('category/<slug:slug_id>', views.show_category, name='category'),
    # path('category_lsit/<int:pk>', views.category_list, name='category_list'),
    path ('all_category/', views.all_category, name='all_category')
]

 