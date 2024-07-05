# Generated by Django 4.2.3 on 2023-08-31 20:59

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_remove_purpose_name_purpose_detail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anthem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100)),
                ('detail', tinymce.models.HTMLField()),
            ],
        ),
    ]
