# Generated by Django 4.1.2 on 2023-05-07 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_press_release_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='press_release',
            name='file',
        ),
    ]
