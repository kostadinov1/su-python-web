# Generated by Django 4.0.2 on 2022-02-21 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_expenses_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expenses',
            old_name='expense_image',
            new_name='image',
        ),
    ]