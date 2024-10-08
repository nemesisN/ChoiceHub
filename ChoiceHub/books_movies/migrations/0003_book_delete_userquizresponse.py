# Generated by Django 5.1 on 2024-09-19 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_movies', '0002_userquizresponse_delete_book_delete_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=100)),
                ('themes', models.CharField(blank=True, max_length=200)),
                ('character_vs_plot', models.CharField(blank=True, choices=[('Character', 'Character-driven'), ('Plot', 'Plot-driven')], max_length=50)),
                ('writing_style', models.CharField(blank=True, max_length=100)),
                ('setting', models.CharField(blank=True, max_length=200)),
                ('mood', models.CharField(blank=True, max_length=100)),
                ('api_source', models.CharField(default='Unknown', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='UserQuizResponse',
        ),
    ]
