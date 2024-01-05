# Generated by Django 5.0 on 2024-01-05 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='landing_phone',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='شماره ثابت'),
        ),
    ]