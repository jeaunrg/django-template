# Generated by Django 4.0.1 on 2022-01-17 16:54

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name="Nom d'utilisateur")),
                ('email', models.EmailField(max_length=60, verbose_name='adresse mail')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to=account.models.upload_location, verbose_name='photo de profile')),
                ('alias', models.CharField(default='--', max_length=200)),
                ('parameters', models.JSONField(blank=True, default=dict)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
