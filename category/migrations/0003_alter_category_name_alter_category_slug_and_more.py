# Generated by Django 4.1.7 on 2023-02-27 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_name_alter_category_parent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=128),
        ),
        migrations.AlterField(
            model_name='main_category',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='main_category',
            name='slug',
            field=models.SlugField(max_length=128),
        ),
        migrations.AlterField(
            model_name='sub_category',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='sub_category',
            name='slug',
            field=models.SlugField(max_length=128),
        ),
    ]