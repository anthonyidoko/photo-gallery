# Generated by Django 3.1.7 on 2021-03-22 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_picture_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to='media/pictures'),
        ),
    ]
