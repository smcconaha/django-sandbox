# Generated by Django 4.1.3 on 2022-11-08 23:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_title_book_titulo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='titulo',
            new_name='title',
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
