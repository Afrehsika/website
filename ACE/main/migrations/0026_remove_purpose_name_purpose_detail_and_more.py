# Generated by Django 4.2.3 on 2023-08-31 17:35

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_history_header'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purpose',
            name='name',
        ),
        migrations.AddField(
            model_name='purpose',
            name='detail',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='PurposeType',
        ),
    ]
