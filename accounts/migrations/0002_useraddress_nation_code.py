# Generated by Django 5.0 on 2024-01-06 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='nation_code',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='کد ملی'),
        ),
    ]