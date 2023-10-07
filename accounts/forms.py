from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, UserAttributes
from django_countries.fields import CountryField


class RegistrationForm(UserCreationForm):
    USER_TYPE_CHOICES = (
        ("student", "Student"),
        ("lecturer", "Lecturer"),
        ("admin", "Admin"),
        ("alumni", "Alumni"),
    )
    user_type = forms.ChoiceField(
        choices=USER_TYPE_CHOICES,
        required=True,  # Set this to True if user_type is required
        widget=forms.Select(
            attrs={"class": "form-control custom-padding form-control-lg"}
        ),
        label="User Type",
    )

    username = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control custom-padding form-control-lg",
                "placeholder": "Username",
            }
        ),
        label="",
    )
    first_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "First Name",
            }
        ),
        label="",
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg", "placeholder": "Last Name"}
        ),
        label="",
    )
    email = forms.EmailField(
        max_length=254,
        required=False,
        widget=forms.EmailInput(
            attrs={"class": "form-control form-control-lg", "placeholder": "Email"}
        ),
        label="",
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control form-control-lg", "placeholder": "Password"}
        ),
        label="",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Repeat Password",
            }
        ),
        label="",
    )

    class Meta:
        model = CustomUser
        fields = [
            "user_type",
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "country",
        ]


class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "password"]  # Fields for login form


class UserAttributesForm(forms.ModelForm):
    GENDER_CHOICES = (
        ("Female", "Female"),
        ("Male", "Male"),
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        required=True,  # Set this to True if user_type is required
        widget=forms.Select(
            attrs={
                "class": "form-control custom-padding form-control-lg",
                "style": "margin-bottom: 10px;",
            }
        ),
        label="",
    )
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "DOB",
                "style": "margin-bottom: 10px;",
            }
        ),
        label="",
    )
    phone = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Phone",
                "style": "margin-bottom: 10px;",
            }
        ),
        label="",
    )
    church_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Church Name",
                "style": "margin-bottom: 10px;",
            }
        ),
        label="",
    )
    nationality = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Nationality",
                "style": "margin-bottom: 10px;",
            }
        ),
        label="",
    )
    address = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Address",
                "style": "margin-bottom: 10px;",
            }
        ),
        label="",
    )
    city = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "City",
                "style": "margin-bottom: 10px;",
            }
        ),
        label="",
    )

    class Meta:
        model = UserAttributes
        fields = [
            "rootID",
            "root",
            "date_of_birth",
            "gender",
            "phone",
            "church_name",
            "nationality",
            "address",
            "city",
            "photo",
        ]
