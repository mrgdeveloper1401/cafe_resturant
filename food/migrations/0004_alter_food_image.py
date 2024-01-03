# Generated by Django 5.0 on 2024-01-01 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_food_description_foodprice_pnnel'),
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='food_images', to='images.images'),
        ),
    ]