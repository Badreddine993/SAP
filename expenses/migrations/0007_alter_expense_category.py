# Generated by Django 3.2.25 on 2024-08-02 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0006_remove_expense_category_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenses.category'),
        ),
    ]
