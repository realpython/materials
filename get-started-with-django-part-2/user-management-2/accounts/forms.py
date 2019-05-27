from django import forms
from django.contrib.auth import password_validation

from accounts.models import User


class LogInForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())


class SetPasswordForm(forms.Form):
    password1 = forms.CharField(
        label="New password", widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label="Confirm password", widget=forms.PasswordInput()
    )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    "The two password fields didn't match."
                )
        password_validation.validate_password(password2)


class PasswordChangeForm(SetPasswordForm):
    old_password = forms.CharField(
        label="Old Password", widget=forms.PasswordInput()
    )
    field_order = ["old_password", "password1", "password2"]


class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label="Email")


class PasswordResetForm(SetPasswordForm):
    pass


class SignUpForm(SetPasswordForm, forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email")
