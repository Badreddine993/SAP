# Generated by Django 3.2.25 on 2024-08-02 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_alter_expense_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='category_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='expenses.category'),
        ),
    ]
