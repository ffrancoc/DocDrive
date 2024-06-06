from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm

class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm()
    model = User


admin.site.register(User, UserAdmin)