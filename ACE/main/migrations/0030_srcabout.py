# Generated by Django 4.2.3 on 2023-09-08 14:53

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_srccarousel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SrcAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100)),
                ('detail', tinymce.models.HTMLField()),
            ],
        ),
    ]