from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email', 'sex', 'avatar']
    # fieldsets = None
    # fields = ['username', 'first_name', 'last_name', 'email', 'sex', 'phone', 'password', 'avatar']
    
    fieldsets = (
        ('Change password', {
            "fields": (
                'password',
            ),
        }),
        ('Personal', {
            'fields': (
                'first_name',
                'last_name',
                'about',
                'avatar',
                'sex',
                'birth_date',
            )
        })
    )
    

admin.site.register(CustomUser, CustomUserAdmin)