from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import *

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'password', 'first_name', 'surname', 'last_name', 'birth_date', 'photo']
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'first_name',
                    'surname',
                    'last_name',
                    'birth_date',
                    'photo',
                    'groups'
                )
            }
        )
    )

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'surname',
                    'birth_date',
                    'photo',
                )
            }
        )
    )