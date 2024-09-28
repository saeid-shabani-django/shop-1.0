from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields=('email', )



