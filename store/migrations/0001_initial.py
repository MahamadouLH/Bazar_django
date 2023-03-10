# Generated by Django 4.1.7 on 2023-02-27 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=256, unique=True)),
                ('slug', models.SlugField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True, max_length=512, null=True)),
                ('price', models.FloatField(default=0.0)),
                ('stock', models.IntegerField(default=0)),
                ('is_available', models.BooleanField(default=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='photos/products')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.main_category')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.sub_category')),
            ],
        ),
    ]
