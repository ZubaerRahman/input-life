from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Blog

from .forms import SignUp, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = SignUp
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email']


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Blog)