# Generated by Django 3.1.3 on 2020-11-25 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('email1', models.EmailField(max_length=254)),
                ('class_name', models.CharField(max_length=100)),
            ],
        ),
    ]