# Generated by Django 5.1.1 on 2024-10-19 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kdapp', '0014_todo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='compleated',
            new_name='completed',
        ),
    ]
