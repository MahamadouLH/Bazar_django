# Generated by Django 4.1.7 on 2023-03-06 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('color', 'color'), ('size', 'size'), ('brand', 'brand'), ('rom_memory', 'rom_memory'), ('ram_memory', 'ram_memory')], max_length=128),
        ),
    ]
