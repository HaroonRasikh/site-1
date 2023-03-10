# Generated by Django 4.1.5 on 2023-01-25 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Anasahifa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=220, null=True)),
                ('logo1', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('logo2', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('logo3', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('logo4', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('logo5', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('logo6', models.ImageField(blank=True, null=True, upload_to='static/images')),
            ],
        ),
    ]
