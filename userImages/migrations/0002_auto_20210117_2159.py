# Generated by Django 3.0 on 2021-01-18 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userImages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='photo',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]