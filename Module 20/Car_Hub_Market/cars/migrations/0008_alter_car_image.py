# Generated by Django 4.2.7 on 2023-12-19 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(upload_to='cars/media/uploads'),
        ),
    ]
