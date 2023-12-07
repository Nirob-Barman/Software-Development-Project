# Generated by Django 4.2.7 on 2023-12-06 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('auto_field', models.AutoField(primary_key=True, serialize=False)),
                ('big_integer_field', models.BigIntegerField()),
                ('binary_field', models.BinaryField()),
                ('boolean_field', models.BooleanField()),
                ('char_field', models.CharField(max_length=255)),
                ('date_field', models.DateField()),
                ('date_time_field', models.DateTimeField()),
                ('decimal_field', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration_field', models.DurationField()),
                ('email_field', models.EmailField(max_length=254)),
                ('float_field', models.FloatField()),
                ('generic_ip_address_field', models.GenericIPAddressField()),
                ('image_field', models.ImageField(upload_to='images/')),
                ('integer_field', models.IntegerField()),
                ('json_field', models.JSONField()),
                ('positive_big_integer_field', models.PositiveBigIntegerField()),
                ('positive_integer_field', models.PositiveIntegerField()),
                ('positive_small_integer_field', models.PositiveSmallIntegerField()),
                ('slug_field', models.SlugField()),
                ('small_integer_field', models.SmallIntegerField()),
                ('text_field', models.TextField()),
                ('time_field', models.TimeField()),
                ('url_field', models.URLField()),
                ('uuid_field', models.UUIDField()),
            ],
        ),
    ]