# Generated by Django 3.2.9 on 2021-11-24 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clean', '0006_auto_20211124_0940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preferences',
            name='columns',
        ),
    ]