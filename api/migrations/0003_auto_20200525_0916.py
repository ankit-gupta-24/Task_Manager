# Generated by Django 3.0.6 on 2020-05-25 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_task_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='timestamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]
