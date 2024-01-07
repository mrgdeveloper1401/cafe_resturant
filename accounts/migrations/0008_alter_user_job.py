# Generated by Django 5.0 on 2024-01-07 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_user_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='job',
            field=models.ManyToManyField(blank=True, related_name='users', to='accounts.job'),
        ),
    ]
