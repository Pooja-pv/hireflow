from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        required=True
    )

    class Meta:

        model = User

        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "role",
            "password1",
            "password2",
        ]

        widgets = {

            "username": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "first_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "last_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "email": forms.EmailInput(
                attrs={"class": "form-control"}
            ),

            "role": forms.Select(
                attrs={"class": "form-select"}
            ),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["password1"].widget.attrs.update({
            "class": "form-control"
        })

        self.fields["password2"].widget.attrs.update({
            "class": "form-control"
        })


class ProfileForm(forms.ModelForm):

    class Meta:

        model = User

        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "bio",
            "skills",
            "profile_image",
        ]

        widgets = {

            "first_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "last_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "email": forms.EmailInput(
                attrs={"class": "form-control"}
            ),

            "phone": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "bio": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5
                }
            ),

            "skills": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder":
                        "Python, Django, MySQL..."
                }
            ),

            "profile_image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control"
                }
            ),
        }