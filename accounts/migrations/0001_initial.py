# Generated by Django 5.0 on 2024-01-06 11:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtpCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_phone', models.CharField(max_length=11, unique=True, verbose_name='شماره موبایل')),
                ('code', models.PositiveIntegerField()),
                ('create_code', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'کد تایید',
                'verbose_name_plural': 'کد تایید',
                'db_table': 'otp_code',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=100, verbose_name='نام')),
                ('last_name', models.CharField(max_length=100, verbose_name='نام خانوادگی')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='ایمیل')),
                ('mobile_phone', models.CharField(max_length=11, unique=True, verbose_name='شماره موبایل')),
                ('is_active', models.BooleanField(default=False, editable=False, verbose_name='کاربر فعال')),
                ('is_staff', models.BooleanField(default=False, editable=False, verbose_name='دسترسی کارمندی')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='درباره خودت')),
                ('address', models.TextField(blank=True, null=True, verbose_name='آدرس کامل')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='عنوان ادرس')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('postal_code', models.CharField(max_length=11, unique=True, verbose_name='کد پستی')),
                ('mobile_phone', models.CharField(max_length=11, unique=True, verbose_name='موبایل')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_address', to=settings.AUTH_USER_MODEL, verbose_name='ادرس کاربر')),
            ],
            options={
                'verbose_name': 'آدرس',
                'verbose_name_plural': 'آدرس ها',
                'db_table': 'user_address',
            },
        ),
    ]
