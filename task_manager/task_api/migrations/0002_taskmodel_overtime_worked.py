# Generated by Django 3.1 on 2020-12-08 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='overtime_worked',
            field=models.FloatField(default=0),
        ),
    ]
