# Generated by Django 4.1.5 on 2023-02-02 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Anasahifa', '0004_social'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selector',
            name='logo1',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='selector',
            name='logo2',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='selector',
            name='logo3',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='selector',
            name='logo4',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='selector',
            name='logo5',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='selector',
            name='logo6',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='selector',
            name='logo7',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
    ]
