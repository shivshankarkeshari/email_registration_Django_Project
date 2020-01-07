# Generated by Django 3.0.2 on 2020-01-07 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.EmailField(max_length=80, unique=True)),
                ('First_Name', models.CharField(max_length=80)),
                ('Last_Name', models.CharField(max_length=80)),
            ],
        ),
    ]
