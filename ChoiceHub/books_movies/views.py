import requests 
from django.shortcuts import render
from .forms import QuizForm
from .models import Book


def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')

# API Key for Google Books
API_KEY = 'YOUR_GOOGLE_BOOKS_API_KEY'

def get_books_from_api(query):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def book_recommendation(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            # Get quiz responses
            genre = form.cleaned_data['genre']
            pace = form.cleaned_data['pace']
            character = form.cleaned_data['character']
            ending = form.cleaned_data['ending']
            setting = form.cleaned_data['setting']
            length = form.cleaned_data['length']
            emotional_tone = form.cleaned_data['emotional_tone']
            romance = form.cleaned_data['romance']
            narrative_style = form.cleaned_data['narrative_style']
            world_building_importance = form.cleaned_data['world_building_importance']

            # Save responses to the database
            UserQuizResponse.objects.create(
                genre_preference=genre,
                pace_preference=pace,
                character_preference=character,
                ending_preference=ending,
                setting_preference=setting,
                length_preference=length,
                emotional_tone_preference=emotional_tone,
                romance_preference=romance,
                narrative_style_preference=narrative_style,
                world_building_importance=world_building_importance
            )

            # Construct API query based on user inputs
            query = f"{genre}+{pace}+{character}+{ending}+{setting}+{length}+{emotional_tone}+{romance}+{narrative_style}+{world_building_importance}"
            books = get_books_from_api(query)

            # Render the template with recommended books
            return render(request, 'recommendation.html', {'books': books['items']})

    else:
        form = QuizForm()

    return render(request, 'quiz.html', {'form': form})