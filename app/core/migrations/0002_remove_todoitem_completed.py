# Generated by Django 4.2.2 on 2023-06-10 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='completed',
        ),
    ]
