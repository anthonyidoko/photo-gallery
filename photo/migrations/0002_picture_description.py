# Generated by Django 3.1.7 on 2021-03-22 15:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=2000),
            preserve_default=False,
        ),
    ]
