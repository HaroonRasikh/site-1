# Generated by Django 4.1.5 on 2023-02-08 13:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(blank=True, max_length=10000, null=True)),
                ('title2', models.CharField(blank=True, max_length=10000, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('facebook', models.CharField(blank=True, max_length=220, null=True)),
                ('twitter', models.CharField(blank=True, max_length=220, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=220, null=True)),
            ],
            options={
                'verbose_name': 'Tablo',
                'verbose_name_plural': 'Tablolar',
            },
        ),
        migrations.CreateModel(
            name='Komanda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=10000, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True)),
            ],
            options={
                'verbose_name': 'Komanda',
                'verbose_name_plural': 'Komanda',
            },
        ),
    ]
