# Generated by Django 5.0 on 2024-01-06 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_productatrribute_attribute_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productatrribute',
            name='attribute_value',
        ),
        migrations.AddField(
            model_name='productattributevalue',
            name='attribute_value',
            field=models.CharField(default=0, max_length=100, verbose_name='مقدار ويژگی'),
            preserve_default=False,
        ),
    ]