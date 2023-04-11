from django.urls import path, include
from goodread_app.api.views import book_list, book_details

urlpatterns = [
    path('list/', book_list, name='book-list'),
    path('<int:pk>/', book_details, name='book-detail'),
]