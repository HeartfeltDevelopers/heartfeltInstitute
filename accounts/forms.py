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
    date_of_birth = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg", "placeholder": "DOB"}
        ),
        label="",
    )
    phone = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg", "placeholder": "Phone"}
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
            }
        ),
        label="",
    )
    address = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg", "placeholder": "Address"}
        ),
        label="",
    )
    city = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg", "placeholder": "City"}
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
            "date_of_birth",
            "phone",
            "church_name",
            "address",
            "city",
            "country",
        ]


class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "password"]  # Fields for login form


class UserAttributesForm(forms.ModelForm):
    date_of_birth = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg", "placeholder": "DOB"}
        ),
        label="",
    )
    phone = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg", "placeholder": "Phone"}
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
            }
        ),
        label="",
    )
    address = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg", "placeholder": "Address"}
        ),
        label="",
    )
    city = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg", "placeholder": "City"}
        ),
        label="",
    )

    class Meta:
        model = UserAttributes
        fields = [
            "rootID",
            "photo",
            "date_of_birth",
            "gender",
            "phone",
            "church_name",
            "nationality",
            "address",
            "city",
            "country",
        ]
