from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    themes = models.CharField(max_length=200, blank=True)
    character_vs_plot = models.CharField(max_length=50, choices=[('Character', 'Character-driven'), ('Plot', 'Plot-driven')], blank=True)
    writing_style = models.CharField(max_length=100, blank=True)
    setting = models.CharField(max_length=200, blank=True)
    mood = models.CharField(max_length=100, blank=True)
    api_source = models.CharField(max_length=100, default="Unknown")  # To track the source API
    
    # New fields
    cover_image = models.URLField(max_length=500, blank=True, null=True)  # Store URL of the cover image
    description = models.TextField(blank=True)  # Store detailed description
    reviews = models.TextField(blank=True, default="Not-available")  # Store reviews
    buy_link = models.URLField(max_length=500, blank=True, default="Not-available")  # Store URL for purchasing the book

    def __str__(self):
        return self.title
