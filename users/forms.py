# flake8: noqa
from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    """Form for user registration.
    Attributes:
        username (str): The username chosen by the user. Must be unique in the system.
        email (str): The email address of the user. Used for account identification and communication.
        password (str): The password for the account. Rendered as a password input for security.
    Meta:
        model (User): The Django User model that this form is creating/editing.
        fields (list): The list of model fields included in the form: username, email, password.
    Note:
        The password field is explicitly defined with `widget=forms.PasswordInput`
        to obscure the input. The form inherits other behavior from ModelForm,
        such as validation tied to the User model.
    """

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password"]
