from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from .forms import QuizForm, LoginForm
from .models import Book, Registration

# View for the index page
def index(request):
    return render(request, 'index.html')

# View to display the list of books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books_movies/book_list.html', {'books': books})

# View for user registration
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if Registration.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'register.html')

        # Create a new registration
        registration = Registration(name=name, email=email, password=password)
        registration.save()  # Password is hashed in the model's save() method

        # Add a success message
        messages.success(request, 'Registration successful!')

        # Log the user in by saving their session
        request.session['user_id'] = registration.id

        return redirect('index')  # Redirect to the home page after registration

    return render(request, 'register.html')

# View for user login
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = Registration.objects.get(email=email)  # Check if email exists
                if check_password(password, user.password):  # Verify password using check_password
                    request.session['user_id'] = user.id  # Save user ID in session
                    messages.success(request, "Login successful!")
                    return redirect('index')  # Redirect to home page after login
                else:
                    messages.error(request, "Invalid login credentials")
            except Registration.DoesNotExist:
                messages.error(request, "User not found. Please register.")
    else:
        form = LoginForm()
    
    return render(request, 'books_movies/login.html', {'form': form})

# View for user logout
def logout_view(request):
    request.session.flush()  # Clear the session data to log out
    return redirect('login')  # Redirect to the login page after logout
