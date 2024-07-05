# Generated by Django 4.2.3 on 2023-09-09 00:56

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_srcbody_srcexecutive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accomodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/srcCarousel')),
                ('hall_name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
            ],
        ),
    ]
