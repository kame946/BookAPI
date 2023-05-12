from django.urls import path
from .views import bookList, about

urlpatterns = [
    path('', bookList, name='home'),
    path('about/', about, name='about'),
]