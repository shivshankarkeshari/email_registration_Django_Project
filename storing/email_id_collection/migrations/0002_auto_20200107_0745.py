# Generated by Django 3.0.2 on 2020-01-07 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_id_collection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.EmailField(max_length=80, unique=True)),
                ('First_Name', models.CharField(max_length=80)),
                ('Last_Name', models.CharField(max_length=80)),
            ],
        ),
        migrations.DeleteModel(
            name='user_data',
        ),
    ]