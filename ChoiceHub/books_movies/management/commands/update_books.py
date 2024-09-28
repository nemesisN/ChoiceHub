from django.core.management.base import BaseCommand
import json
from books_movies.models import Book  # Import your Book model

class Command(BaseCommand):
    help = 'Update book fields from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('books_movies/books_data.json', type=str, help='The path to the JSON file')

    def handle(self, *args, **options):
        book_data = []
        file_path = options['books_movies/books_data.json']

        try:
            with open(file_path, mode='r', encoding='utf-8') as jsonfile:
                book_data = json.load(jsonfile)  # Load JSON data

            self.update_books(book_data)
            self.stdout.write(self.style.SUCCESS('Successfully updated books from JSON'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Error decoding JSON file'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))

    def update_books(self, book_data):
        for book in book_data:
            book_title = book.get("title")
            # Try to retrieve the existing book instance by title
            try:
                book_instance = Book.objects.get(title=book_title)

                # Only update fields that are present in the JSON file
                updated_fields = {}
                for field in [
                    "author", "genre", "themes", "character_vs_plot",
                    "writing_style", "setting", "mood", "cover_image",
                    "length", "pace", "character", "ending",
                    "emotional_tone", "romance", "narrative_style",
                    "world_building_importance", "api_source"
                ]:
                    if field in book:
                        updated_fields[field] = book[field]

                # Update the instance with new values if they exist
                for key, value in updated_fields.items():
                    setattr(book_instance, key, value)

                book_instance.save()  # Save the updated instance
                self.stdout.write(self.style.SUCCESS(f'Updated book: {book_title}'))
            except Book.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Book not found: {book_title}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error updating book {book_title}: {str(e)}'))