from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from .forms import LoginForm
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


from django.shortcuts import render
from .models import Book
from django.shortcuts import render, redirect
from .forms import BookPreferenceForm
from .models import Book


def book_quiz_view(request):
    temp_db1 = list(Book.objects.all())  # Start with all books
    temp_db2 = []

    if request.method == 'POST':
        form = BookPreferenceForm(request.POST)
        
        if form.is_valid():
            answers = form.cleaned_data
            
            # Print the answers to debug
            print("User Answers:", answers)
            
            for question, answer in answers.items():
                print(f"Filtering by {question}: {answer}")  # Debugging statement
                temp_db2 = []

                # Check if the remaining books are 4 or fewer
                # if len(temp_db1) <= 4:
                #     print("Book count is 4 or fewer, stopping further filtering.")
                #     break

                for book in temp_db1:
                    # print(getattr(book, question))
                    if getattr(book, question) == answer:
                        temp_db2.append(book)
                
                # After filtering, assign the new filtered list to temp_db1
                if len(temp_db2) <= 4:
                    print("Book count is 4 or fewer, stopping further filtering.")
                    break
                temp_db1 = temp_db2
                print(f"Filtered Books: {temp_db1}")

                # Again check if the remaining books are 4 or fewer
            
            # After filtering or stopping, render the final filtered book list
            return render(request, 'books_movies/filtered_books.html', {'books': temp_db1})

    else:
        form = BookPreferenceForm()
    
    return render(request, 'books_movies/quiz.html', {'form': form})


