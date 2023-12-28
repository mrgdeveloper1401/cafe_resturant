# Generated by Django 5.0 on 2023-12-28 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='ایمیل')),
                ('mobile_phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='شماره موبایل')),
                ('description', models.TextField(verbose_name='توضحات')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='محل شعبه')),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'تماس با ما',
                'db_table': 'contact_us',
            },
        ),
    ]