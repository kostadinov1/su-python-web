# Generated by Django 4.0.2 on 2022-02-19 10:30

import django.core.validators
from django.db import migrations, models
import exam_prep_1.main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_expenses_profile_budget_profile_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), exam_prep_1.main_app.models.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), exam_prep_1.main_app.models.validate_only_letters]),
        ),
    ]
