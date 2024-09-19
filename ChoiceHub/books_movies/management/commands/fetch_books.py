# books_movies/management/commands/fetch_books.py

from django.core.management.base import BaseCommand
import requests
from books_movies.models import Book

# API Key for Google Books
API_KEY = 'YOUR_GOOGLE_BOOKS_API_KEY'

class Command(BaseCommand):
    help = 'Fetch and save books from Google Books API'

    def add_arguments(self, parser):
        parser.add_argument(
            '--query',
            type=str,
            default='',
            help='Search query for Google Books API'
        )

    def handle(self, *args, **options):
        query = options['query']
        if not query:
            self.stdout.write(self.style.ERROR('No query provided. Use the --query argument to specify a search term.'))
            return

        url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={API_KEY}"
        response = requests.get(url)
        
        if response.status_code == 200:
            try:
                books_data = response.json()
                items = books_data.get('items', [])
                
                for item in items:
                    volume_info = item.get('volumeInfo', {})
                    
                    Book.objects.create(
                        title=volume_info.get('title', 'N/A'),
                        author=', '.join(volume_info.get('authors', [])),
                        genre=', '.join(volume_info.get('categories', [])),
                        length=volume_info.get('pageCount', 'N/A'),
                        pace='N/A',  # Adjust based on available data
                        character='N/A',  # Adjust based on available data
                        ending='N/A',  # Adjust based on available data
                        setting='N/A',  # Adjust based on available data
                        emotional_tone='N/A',  # Adjust based on available data
                        romance='N/A',  # Adjust based on available data
                        narrative_style='N/A',  # Adjust based on available data
                        world_building_importance='N/A'  # Adjust based on available data
                    )
                
                self.stdout.write(self.style.SUCCESS('Books fetched and saved successfully!'))

            except requests.exceptions.JSONDecodeError as e:
                self.stdout.write(self.style.ERROR(f"Error parsing JSON: {e}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))

        else:
            self.stdout.write(self.style.ERROR(f"API request failed with status code {response.status_code}"))
