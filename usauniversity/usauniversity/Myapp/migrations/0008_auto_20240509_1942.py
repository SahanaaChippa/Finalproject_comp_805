# Generated by Django 3.1.1 on 2024-05-09 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0007_university'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saveduniversity',
            name='user',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='SavedUniversity',
        ),
    ]
