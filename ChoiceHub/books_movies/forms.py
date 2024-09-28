from django import forms

from django import forms

class BookPreferenceForm(forms.Form):
    genre = forms.ChoiceField(
        label='What genre are you interested in?', 
        choices=[
            ('Philosophy', 'Philosophy'),
            ('Art & Architecture', 'Art & Architecture'),
            ('Non-fiction', 'Non-fiction'),
            ('Art', 'Art'),
            ('Biography & Autobiography', 'Biography & Autobiography'),
            ('Fiction', 'Fiction'),
            ('Social Science', 'Social Science'),
            ('Drama', 'Drama'),
            ('Music', 'Music'),
            ('History', 'History'),
            ('Art History', 'Art History'),
            ('Education', 'Education'),
            ('Cultural Studies', 'Cultural Studies'),
            ('Poetry', 'Poetry'),
            ('Art Instruction', 'Art Instruction'),
            ('Photography', 'Photography'),
            ('Environmental Studies', 'Environmental Studies'),
            ('Self-help', 'Self-help'),
            ('Children\'s Literature', 'Children\'s Literature'),
            ('Reference', 'Reference'),
            ('Travel', 'Travel'),
            ('Science', 'Science'),
            ('Neuroscience', 'Neuroscience'),
            ('Art Therapy', 'Art Therapy')
        ]
    )

    writing_style = forms.ChoiceField(
        label='What type of writing style do you prefer?',
        choices=[
            ('Analytical', 'Analytical'),
            ('Descriptive', 'Descriptive'),
            ('Narrative', 'Narrative'),
            ('Conversational', 'Conversational'),
            ('Lyric', 'Lyric'),
            ('Technical', 'Technical')
        ]
    )

    setting = forms.ChoiceField(
        label='What type of setting do you prefer?',
        choices=[
            ('Contemporary', 'Contemporary'),
            ('Historical', 'Historical'),
            ('Fairytale', 'Fairytale')
        ]
    )

    mood = forms.ChoiceField(
        label='What kind of mood are you looking for?',
        choices=[
            ('Reflective', 'Reflective'),
            ('Engaging', 'Engaging'),
            ('Serious', 'Serious'),
            ('Light-hearted', 'Light-hearted'),
            ('Thought-provoking', 'Thought-provoking'),
            ('Inspirational', 'Inspirational'),
            ('Dramatic', 'Dramatic'),
            ('Bittersweet', 'Bittersweet'),
            ('Hopeful', 'Hopeful'),
            ('Informative', 'Informative'),
            ('Critical', 'Critical'),
            ('Joyful', 'Joyful'),
            ('Dark', 'Dark'),
            ('Nostalgic', 'Nostalgic'),
            ('Educational', 'Educational')
        ]
    )

    length = forms.ChoiceField(
        label='What book length do you prefer?',
        choices=[
            ('Short (Under 100 pages)', 'Short (Under 100 pages)'),
            ('Medium (100-300 pages)', 'Medium (100-300 pages)'),
            ('Long (300-500 pages)', 'Long (300-500 pages)'),
            ('Epic (Over 500 pages)', 'Epic (Over 500 pages)')
        ]
    )

    pace = forms.ChoiceField(
        label='Do you prefer fast-paced or slow-paced books?',
        choices=[
            ('Steady', 'Steady'),
            ('Fast-paced', 'Fast-paced'),
            ('Moderate', 'Moderate')
        ]
    )

    ending = forms.ChoiceField(
        label='What kind of ending do you prefer?',
        choices=[
            ('Open-ended', 'Open-ended'),
            ('Conclusive', 'Conclusive'),
            ('Ambiguous', 'Ambiguous')
        ]
    )

    emotional_tone = forms.ChoiceField(
        label='What kind of emotional tone do you prefer?',
        choices=[
            ('Thought-provoking', 'Thought-provoking'),
            ('Inspirational', 'Inspirational'),
            ('Hopeful', 'Hopeful'),
            ('Bittersweet', 'Bittersweet'),
            ('Informative', 'Informative'),
            ('Dramatic', 'Dramatic'),
            ('Joyful', 'Joyful'),
            ('Melancholic', 'Melancholic'),
            ('Neutral', 'Neutral'),
            ('Educational', 'Educational'),
            ('Nostalgic', 'Nostalgic'),
            ('Philosophical', 'Philosophical'),
            ('Intense', 'Intense')
        ]
    )

    romance = forms.ChoiceField(
        label='What level of romance do you prefer in a book?',
        choices=[
            ('Non-existent', 'Non-existent'),
            ('Minimal', 'Minimal'),
            ('Subplot', 'Subplot'),
            ('Complicated', 'Complicated'),
            ('Central to the plot', 'Central to the plot')
        ]
    )

    narrative_style = forms.ChoiceField(
        label='What narrative style do you prefer?',
        choices=[
            ('Third-person', 'Third-person'),
            ('First-person', 'First-person'),
            ('Second-person', 'Second-person')
        ]
    )

    world_building_importance = forms.ChoiceField(
        label='How important is world-building to you?',
        choices=[
            ('Low importance', 'Low importance'),
            ('Moderate importance', 'Moderate importance'),
            ('High importance', 'High importance')
        ]
    )


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

