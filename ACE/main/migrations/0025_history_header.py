# Generated by Django 4.2.3 on 2023-08-31 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_remove_purposetype_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='header',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
