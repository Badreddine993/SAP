# Generated by Django 3.2.25 on 2024-08-02 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0005_expense_category_fk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='category_fk',
        ),
    ]
