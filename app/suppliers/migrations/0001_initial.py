# Generated by Django 3.2.7 on 2021-09-14 02:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('supplier_name', models.CharField(max_length=255, unique=True, verbose_name="supplier's name")),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=255, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('district', models.CharField(choices=[('Gros Islet', 'Gros Islet'), ('Castries', 'Castries'), ('Soufriere', 'Soufriere'), ('Vieux Fort', 'Vieux Fort')], default='Castries', max_length=25)),
                ('website', models.URLField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('tags', models.TextField(blank=True, help_text='Tags separated by comma eg.: #tag, #tags', null=True)),
                ('created_by', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supplier_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supplier_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['supplier_name'],
            },
        ),
    ]
