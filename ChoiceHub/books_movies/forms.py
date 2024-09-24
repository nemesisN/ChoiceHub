from django import forms

class QuizForm(forms.Form):
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
    
    # New questions
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
    
    # Fields for new questions
    genre = forms.ChoiceField(choices=GENRE_CHOICES)
    pace = forms.ChoiceField(choices=PACE_CHOICES)
    character = forms.ChoiceField(choices=CHARACTER_CHOICES)
    ending = forms.ChoiceField(choices=ENDING_CHOICES)
    setting = forms.ChoiceField(choices=SETTING_CHOICES)
    length = forms.ChoiceField(choices=LENGTH_CHOICES)
    emotional_tone = forms.ChoiceField(choices=EMOTIONAL_TONE_CHOICES)
    romance = forms.ChoiceField(choices=ROMANCE_CHOICES)
    narrative_style = forms.ChoiceField(choices=NARRATIVE_STYLE_CHOICES)
    world_building_importance = forms.ChoiceField(choices=WORLD_BUILDING_IMPORTANCE_CHOICES)

# forms.py

# forms.py
from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

