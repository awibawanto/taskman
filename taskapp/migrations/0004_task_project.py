# Generated by Django 2.2.1 on 2019-05-04 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0003_auto_20190504_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='taskapp.Project'),
            preserve_default=False,
        ),
    ]
