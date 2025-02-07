from django.shortcuts import render
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, 'reading/index.html', {'books': books})

def info(request, book_id):
    book = Book.objects.get(pk=id)
    return render(request, 'reading/info.html', {'book': book})
