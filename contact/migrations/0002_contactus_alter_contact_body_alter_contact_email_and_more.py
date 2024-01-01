# Generated by Django 5.0 on 2024-01-01 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
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
        migrations.AlterField(
            model_name='contact',
            name='body',
            field=models.TextField(verbose_name='متن'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobile_phone',
            field=models.CharField(max_length=11, verbose_name='شماره همراه'),
        ),
    ]
