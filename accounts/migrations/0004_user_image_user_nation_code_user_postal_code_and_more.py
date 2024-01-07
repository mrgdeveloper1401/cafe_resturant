# Generated by Django 5.0 on 2024-01-07 06:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_job'),
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='images.images'),
        ),
        migrations.AddField(
            model_name='user',
            name='nation_code',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='کد ملی'),
        ),
        migrations.AddField(
            model_name='user',
            name='postal_code',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='کد پستی'),
        ),
        migrations.RemoveField(
            model_name='job',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserAddress',
        ),
        migrations.AddField(
            model_name='job',
            name='user',
            field=models.ManyToManyField(related_name='jobs', to=settings.AUTH_USER_MODEL),
        ),
    ]