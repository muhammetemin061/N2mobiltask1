# Generated by Django 5.1.1 on 2024-09-21 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kdapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='adress',
            field=models.JSONField(default=dict, help_text='adres json '),
        ),
    ]