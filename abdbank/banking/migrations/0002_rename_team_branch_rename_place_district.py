# Generated by Django 4.2 on 2023-04-12 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='team',
            new_name='branch',
        ),
        migrations.RenameModel(
            old_name='place',
            new_name='district',
        ),
    ]
