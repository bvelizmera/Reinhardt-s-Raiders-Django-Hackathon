# Generated by Django 4.2.11 on 2024-03-07 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_remove_event_attending_event_attending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attending',
            field=models.ManyToManyField(blank=True, related_name='attending', to='event.student'),
        ),
    ]
