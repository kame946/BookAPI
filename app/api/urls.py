from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveUpdateAPIView

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book-list'),
    path('books/<int:pk>', BookRetrieveUpdateAPIView.as_view(), name='book-detail'),
]