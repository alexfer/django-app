# Generated by Django 4.0 on 2022-11-20 13:29

import content.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('content', '0002_alter_entry_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.ImageField(null=True, upload_to=content.models.Entry.entry_directory_path),
        ),
    ]
