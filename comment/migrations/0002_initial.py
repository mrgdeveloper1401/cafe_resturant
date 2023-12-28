# Generated by Django 5.0 on 2023-12-28 17:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comment', '0001_initial'),
        ('food', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comment_food', to='food.food'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reply',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reply_comment_food', to='food.food'),
        ),
        migrations.AddField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reply_user_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]