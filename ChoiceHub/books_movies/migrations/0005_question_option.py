# Generated by Django 5.1 on 2024-09-19 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_movies', '0004_book_buy_link_book_cover_image_book_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('genre_score', models.CharField(blank=True, max_length=100, null=True)),
                ('mood_score', models.CharField(blank=True, max_length=100, null=True)),
                ('writing_style_score', models.CharField(blank=True, max_length=100, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='books_movies.question')),
            ],
        ),
    ]
