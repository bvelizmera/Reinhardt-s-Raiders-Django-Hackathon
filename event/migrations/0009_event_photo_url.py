# Generated by Django 4.2.11 on 2024-03-08 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_merge_20240308_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='photo_url',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
