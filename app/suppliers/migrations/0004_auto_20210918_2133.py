# Generated by Django 3.2.7 on 2021-09-19 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0003_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='category',
        ),
        migrations.AddField(
            model_name='supplier',
            name='category',
            field=models.ManyToManyField(blank=True, to='suppliers.Category'),
        ),
    ]
