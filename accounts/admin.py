from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import CustomUser
from .forms import UserChangeForm, UserCreationForm, CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email','username', )
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm


