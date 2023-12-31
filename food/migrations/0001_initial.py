# Generated by Django 5.0 on 2024-01-05 07:18

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0001_initial'),
        ('pannel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='عنوان')),
                ('slug', models.SlugField(allow_unicode=True, unique=True, verbose_name='اسلاگ')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='category_images', to='images.images')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='food.category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('food_name', models.CharField(max_length=100, verbose_name='نام غذا')),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True, verbose_name='slug')),
                ('food_number', models.PositiveSmallIntegerField(default=0, verbose_name='تعداد غذاهای موجود')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_get_out', models.BooleanField(default=True, verbose_name='بیرون بر')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیح در مورد غذا')),
                ('is_avaliable', models.BooleanField(default=True, verbose_name='غذا موجود هست')),
                ('buy_price', models.PositiveIntegerField(default=0, verbose_name='قیمت خرید')),
                ('sell_price', models.PositiveIntegerField(default=0, verbose_name='قیمت فروش')),
                ('discount', models.PositiveIntegerField(default=0, verbose_name='تخفیف')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category_food', to='food.category')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='food_images', to='images.images')),
                ('pannel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pannel_food', to='pannel.pannel')),
            ],
            options={
                'verbose_name': 'غذا',
                'verbose_name_plural': 'غذاها',
                'db_table': 'food',
            },
        ),
    ]
