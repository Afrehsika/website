# Generated by Django 4.2.3 on 2023-08-31 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_anthem'),
    ]

    operations = [
        migrations.AddField(
            model_name='principal',
            name='header',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
