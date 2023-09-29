from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from auth_and_perms.models import User
from commerce.models import Client


class ClientSignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
        ]

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'username': 'Username'
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your first name',
                    'id': 'first_name',
                    'required': 'required'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your last name',
                    'id': 'last_name',
                    'required': 'required'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your email',
                    'id': 'email',
                    'required': 'required'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Create a unique username',
                    'id': 'username',
                    'required': 'required'
                }
            ),
            'password1': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter a password',
                    'id': 'password',
                    'required': 'required'
                }
            )
        }

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        client = Client.objects.create(
            first_name=user.first_name,
            last_name=user.last_name,
            user=user,
        )

        return user
