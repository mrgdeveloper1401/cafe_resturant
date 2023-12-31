# Generated by Django 5.0 on 2024-01-05 07:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('food', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title_comment', models.CharField(max_length=255, verbose_name='عنوان')),
                ('content_comment', models.TextField(verbose_name='متن')),
                ('slug', models.SlugField(allow_unicode=True, max_length=155, unique=True, verbose_name='نام ��ناسه')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال')),
                ('rate_choose', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=5, verbose_name='امتیاز')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comment_food', to='food.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_comment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظرات',
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('body', models.TextField(verbose_name='متن')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reply_comment_food', to='food.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reply_user_comment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'پاسخ نظر',
                'verbose_name_plural': 'پاسخ نظرات',
                'db_table': 'reply_comment',
            },
        ),
    ]
