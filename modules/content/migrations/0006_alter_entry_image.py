# Generated by Django 4.0 on 2022-11-21 05:13

from django.db import migrations, models
import modules


class Migration(migrations.Migration):
    dependencies = [
        ('content', '0005_alter_entry_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(default='placeholder.png', null=True,
                                    upload_to=modules.content.models.Entry.entry_directory_path),
        ),
    ]
