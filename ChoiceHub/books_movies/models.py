from django.db import models

class Book(models.Model):
    GENRE_CHOICES = [
        ('mystery', 'Mystery/Thriller'),
        ('scifi', 'Science Fiction/Fantasy'),
        ('romance', 'Romance'),
        ('historical', 'Historical Fiction'),
    ]
    PACE_CHOICES = [
        ('fast', 'Fast-paced'),
        ('medium', 'Medium-paced'),
        ('slow', 'Slow-paced'),
        ('any', 'It doesn’t matter'),
    ]
    CHARACTER_CHOICES = [
        ('hero', 'Brave hero/heroine'),
        ('underdog', 'Underdog'),
        ('complex', 'Morally complex'),
        ('dreamer', 'Dreamer/visionary'),
    ]
    ENDING_CHOICES = [
        ('happy', 'Happy ending'),
        ('bittersweet', 'Bittersweet ending'),
        ('cliffhanger', 'Cliffhanger'),
        ('open', 'Open-ended'),
    ]
    SETTING_CHOICES = [
        ('dystopian', 'Dystopian world'),
        ('magical', 'Magical land'),
        ('historical', 'Historical time period'),
        ('contemporary', 'Contemporary, real-world setting'),
    ]
    LENGTH_CHOICES = [
        ('short', 'Short (under 200 pages)'),
        ('medium', 'Medium (200-400 pages)'),
        ('long', 'Long (400-600 pages)'),
        ('very_long', 'Very long (over 600 pages)'),
    ]
    EMOTIONAL_TONE_CHOICES = [
        ('lighthearted', 'Light-hearted'),
        ('dark', 'Dark and intense'),
        ('inspirational', 'Inspirational'),
        ('emotional', 'Emotional and heartfelt'),
    ]
    ROMANCE_CHOICES = [
        ('yes', 'Yes, I love it'),
        ('moderate', 'Yes, but in moderation'),
        ('minimal', 'Minimal romance'),
        ('none', 'No romance at all'),
    ]
    NARRATIVE_STYLE_CHOICES = [
        ('first_person', 'First-person'),
        ('third_person', 'Third-person'),
        ('multiple_povs', 'Multiple points of view'),
        ('epistolary', 'Epistolary (letters, diary entries, etc.)'),
    ]
    WORLD_BUILDING_IMPORTANCE_CHOICES = [
        ('extremely', 'Extremely important'),
        ('somewhat', 'Somewhat important'),
        ('not_very', 'Not very important'),
        ('not_at_all', 'Not important at all'),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    length = models.CharField(max_length=50, choices=LENGTH_CHOICES)
    pace = models.CharField(max_length=50, choices=PACE_CHOICES)
    character = models.CharField(max_length=50, choices=CHARACTER_CHOICES)
    ending = models.CharField(max_length=50, choices=ENDING_CHOICES)
    setting = models.CharField(max_length=50, choices=SETTING_CHOICES)
    emotional_tone = models.CharField(max_length=50, choices=EMOTIONAL_TONE_CHOICES)
    romance = models.CharField(max_length=50, choices=ROMANCE_CHOICES)
    narrative_style = models.CharField(max_length=50, choices=NARRATIVE_STYLE_CHOICES)
    world_building_importance = models.CharField(max_length=50, choices=WORLD_BUILDING_IMPORTANCE_CHOICES)

    def _str_(self):
        return self.title