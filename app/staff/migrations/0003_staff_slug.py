# Generated by Django 3.2.7 on 2021-09-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_alter_staff_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]
