# Generated by Django 4.2.3 on 2023-08-30 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='category',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='details',
            field=models.TextField(),
        ),
    ]