from django.shortcuts import render,get_object_or_404
from .models import Blogs,Book
# Create your views here.

def home(request):
    return render(request,'home.html')

def blog(request):
    # Group entries by category
    categories = {}
    for entry in Blogs.objects.all():
        categories.setdefault(entry.category, []).append(entry)
    
    return render(request, 'blog.html', {'categories': categories})

def book_list(request):
    books = Book.objects.all()  # Fetches all Book records from the database
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'books/book_detail.html', {'book': book})