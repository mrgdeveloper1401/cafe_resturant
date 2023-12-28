# Generated by Django 5.0 on 2023-12-28 17:10

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
            name='Sciol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('sciol_name', models.CharField(max_length=155, verbose_name='نام شبکه مجازی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
            ],
            options={
                'verbose_name': 'شبکه مجازی',
                'verbose_name_plural': 'شبکه مجازی',
                'db_table': 'sciol',
            },
        ),
        migrations.CreateModel(
            name='Pannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='food_pannel', to='food.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_pannel', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SciolValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('value', models.URLField(max_length=255, verbose_name='مقدار')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیح')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('pannel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contact_pannel_values', to='pannel.pannel')),
                ('sciol', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sciol_values', to='pannel.sciol')),
            ],
            options={
                'verbose_name': 'مقدار شبکه مجازی',
                'verbose_name_plural': 'مقدار شبکه مجازی',
                'db_table': 'sciol_values',
            },
        ),
    ]
