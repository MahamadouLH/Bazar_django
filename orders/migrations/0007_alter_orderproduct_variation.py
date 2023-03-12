# Generated by Django 4.1.7 on 2023-03-10 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_variation_variation_category'),
        ('orders', '0006_alter_orderproduct_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='variation',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='store.variation'),
            preserve_default=False,
        ),
    ]
