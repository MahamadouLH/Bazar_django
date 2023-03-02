# Generated by Django 4.1.7 on 2023-02-27 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='category', to='category.main_category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='sub_category',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='sub_category', to='category.category'),
        ),
    ]