from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser



class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['user_type', 'username', 'first_name', 'last_name', 'date_of_birth', 'email', 'phone', 'church_name', 'password1',
                  'password2', 'address', 'city', 'country']


class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']  # Fields for login form
