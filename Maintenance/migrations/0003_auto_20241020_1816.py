# Generated by Django 3.2.25 on 2024-10-20 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Maintenance', '0002_auto_20241020_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumtask',
            name='date_completed',
        ),
        migrations.RemoveField(
            model_name='forumtask',
            name='duration',
        ),
    ]
