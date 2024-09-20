from django.shortcuts import render, redirect
import requests
from .models import Book
from .models import Registration
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

# books/views.py
from .models import Book

# View to display all books in the database
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

from .models import Registration

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if Registration.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already exists'})

        registration = Registration(name=name, email=email, password=password)
        registration.save()

        # Add a success message
        messages.success(request, 'Registration successful!')

        return redirect('index')  # Redirect to the home page

    return render(request, 'register.html')

 # Point to your success template