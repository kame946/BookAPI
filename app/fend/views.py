from django.shortcuts import render
import requests

# Create your views here.

# Consuming my api
def bookList(request):
    response = requests.get('http://localhost:8000/api/books/')
    books = response.json()

    return render(request, 'fend/index.html', {'books':books})

def about(request):
    return render(request, 'fend/about.html')