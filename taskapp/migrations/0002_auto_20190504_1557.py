# Generated by Django 2.2.1 on 2019-05-04 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.CharField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(default='', max_length=128),
        ),
    ]
