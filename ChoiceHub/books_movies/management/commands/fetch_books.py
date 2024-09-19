# books/management/commands/fetch_books.py

import requests
from django.core.management.base import BaseCommand
from books_movies.models import Book

class Command(BaseCommand):
    help = 'Fetch all books from an external API and store them in the database'

    def handle(self, *args, **kwargs):
        genres = [
            'art', 'biography', 'computers', 'fantasy', 'historical fiction', 
            'horror', 'mystery', 'romance', 'science fiction', 'thriller', 
            'young adult', 'children', 'non-fiction', 'self-help', 
            'health', 'business', 'travel', 'cookbooks', 'education'
        ]

        max_results_per_request = 40
        for genre in genres:
            start_index = 0
            total_items = float('inf')

            while start_index < total_items:
                api_url = f"https://www.googleapis.com/books/v1/volumes?q=subject:{genre.replace(' ', '+')}&startIndex={start_index}&maxResults={max_results_per_request}"
                response = requests.get(api_url)

                if response.status_code == 200:
                    books_data = response.json()
                    total_items = books_data.get('totalItems', 0)

                    if total_items == 0:
                        break

                    for item in books_data.get('items', []):
                        volume_info = item['volumeInfo']
                        title = volume_info.get('title', '')
                        author = ', '.join(volume_info.get('authors', []))
                        book_genre = volume_info.get('categories', ['unknown'])[0]
                        description = volume_info.get('description', '')

                        # Populate new fields
                        length = 'medium'  # Adjust as necessary
                        pace = 'medium'    # Adjust as necessary
                        character = 'hero' # Adjust as necessary
                        ending = 'open'    # Adjust as necessary
                        setting = 'contemporary'  # Adjust as necessary
                        emotional_tone = 'lighthearted'  # Adjust as necessary
                        romance = 'none'  # Adjust as necessary
                        narrative_style = 'third_person'  # Adjust as necessary
                        world_building_importance = 'somewhat'  # Adjust as necessary

                        book_exists = Book.objects.filter(title=title, author=author).exists()

                        if not book_exists:
                            Book.objects.create(
                                title=title,
                                author=author,
                                genre=book_genre,
                                themes=description[:200],  # Using a portion of the description for themes.
                                character_vs_plot='Character' if 'character' in description.lower() else 'Plot',
                                writing_style='Fast-paced' if len(description) < 500 else 'Descriptive',
                                setting=setting,
                                mood='Dark' if 'mystery' in description.lower() else 'Light-hearted',
                                cover_image=volume_info.get('imageLinks', {}).get('thumbnail', ''),
                                length=length,
                                pace=pace,
                                character=character,
                                ending=ending,
                                emotional_tone=emotional_tone,
                                romance=romance,
                                narrative_style=narrative_style,
                                world_building_importance=world_building_importance,
                                api_source='Google Books API'
                            )
                            self.stdout.write(self.style.SUCCESS(f'Successfully added book: {title}'))
                        else:
                            self.stdout.write(self.style.WARNING(f'Book "{title}" by {author} already exists. Skipping...'))

                    start_index += max_results_per_request
                else:
                    self.stdout.write(self.style.ERROR(f"Failed to fetch data for genre: {genre}. Status code: {response.status_code}"))
                    break