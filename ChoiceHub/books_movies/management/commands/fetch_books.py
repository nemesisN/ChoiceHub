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
                        book_info = item['volumeInfo']
                        title = book_info.get('title', 'Unknown Title')
                        author = ', '.join(book_info.get('authors', ['Unknown Author']))
                        book_genre = ', '.join(book_info.get('categories', ['Unknown Genre']))
                        description = book_info.get('description', '')
                        
                        # Fetch higher quality cover image, if available
                        image_links = book_info.get('imageLinks', {})
                        cover_image = image_links.get('extraLarge', '') or \
                                      image_links.get('large', '') or \
                                      image_links.get('medium', '') or \
                                      image_links.get('thumbnail', '')

                        # Fetch reviews if available (Google Books might not provide reviews, so placeholder is used)
                        reviews = book_info.get('averageRating', 'Not-available')

                        # Fetch buy link if available, otherwise 'Not-available'
                        buy_link = item.get('saleInfo', {}).get('buyLink', 'Not-available')

                        # Logic to derive other details
                        themes = description[:200] if description else 'Not-available'
                        character_vs_plot = 'Character' if 'character' in description.lower() else 'Plot'
                        writing_style = 'Fast-paced' if len(description) < 500 else 'Descriptive'
                        setting = 'Unknown'
                        mood = 'Dark' if 'mystery' in description.lower() else 'Light-hearted'

                        # Check if the book already exists in the database
                        book_exists = Book.objects.filter(title=title, author=author).exists()

                        if not book_exists:
                            # Create a new book record
                            Book.objects.create(
                                title=title,
                                author=author,
                                genre=book_genre,
                                themes=themes,
                                character_vs_plot=character_vs_plot,
                                writing_style=writing_style,
                                setting=setting,
                                mood=mood,
                                api_source='Google Books API',
                                cover_image=cover_image,  # Store high-quality cover image
                                description=description,
                                reviews=reviews,  # Store real reviews or placeholder
                                buy_link=buy_link  # Store buy link or 'Not-available'
                            )
                            self.stdout.write(self.style.SUCCESS(f'Successfully added book: {title}'))
                        else:
                            self.stdout.write(self.style.WARNING(f'Book "{title}" by {author} already exists. Skipping...'))

                    start_index += max_results_per_request
                else:
                    self.stdout.write(self.style.ERROR(f"Failed to fetch data for genre: {genre}. Status code: {response.status_code}"))
                    break
