# Generated by Django 4.2.11 on 2024-06-01 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskcategory',
            name='tasks',
        ),
    ]
