# Generated by Django 4.2.7 on 2023-12-06 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mymodel',
            name='image_field',
        ),
    ]
