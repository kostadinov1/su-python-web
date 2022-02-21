from django.contrib import admin
from exam_prep_1.main_app.models import Expenses, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Expenses)
class Expenses(admin.ModelAdmin):
    pass
