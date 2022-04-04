# Generated by Django 4.0.2 on 2022-02-26 22:49

import algorithm.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name="Nom de l'algorithme")),
                ('layout', models.FileField(default='D:\\Developpement\\AFinalProject\\django-template\\mysite\\media_cdn\\default\\algorithm\\layout.xlsx', upload_to=algorithm.models.upload_layout)),
                ('questions', models.FileField(default='D:\\Developpement\\AFinalProject\\django-template\\mysite\\media_cdn\\default\\algorithm\\questions.xlsx', upload_to=algorithm.models.upload_questions)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]