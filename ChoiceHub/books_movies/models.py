from django.db import models
from django.contrib.auth.hashers import make_password

class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Ensures email is unique
    password = models.CharField(max_length=128)  # Store hashed password

    def save(self, *args, **kwargs):
        # Hash the password before saving
        if self.pk is None:  # Only hash if it's a new registration
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.email}'



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    themes = models.CharField(max_length=200, blank=True)
    character_vs_plot = models.CharField(max_length=50, choices=[('Character', 'Character-driven'), ('Plot', 'Plot-driven')], blank=True)
    writing_style = models.CharField(max_length=100, blank=True)
    setting = models.CharField(max_length=200, blank=True)
    mood = models.CharField(max_length=100, blank=True)
    cover_image = models.URLField(max_length=200, blank=True)
    
    # New fields
    length = models.CharField(max_length=100, default='medium')
    pace = models.CharField(max_length=100, default='medium')
    character = models.CharField(max_length=100, default='hero')
    ending = models.CharField(max_length=100, default='open')
    emotional_tone = models.CharField(max_length=100, default='lighthearted')
    romance = models.CharField(max_length=100, default='none')
    narrative_style = models.CharField(max_length=100, default='third_person')
    world_building_importance = models.CharField(max_length=100, default='somewhat')
    
    api_source = models.CharField(max_length=100, default="Unknown")

    def __str__(self):
        return self.title