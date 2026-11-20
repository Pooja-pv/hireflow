from django import forms

from .models import Application


class ApplicationForm(
    forms.ModelForm
):

    class Meta:

        model = Application

        fields = [
            "resume",
            "cover_letter"
        ]

        widgets = {

            "resume": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": ".pdf,.doc,.docx"
                }
            ),

            "cover_letter": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 7,
                    "placeholder":
                        "Write your cover letter..."
                }
            ),
        }

    def __init__(
        self,
        *args,
        **kwargs
    ):

        super().__init__(
            *args,
            **kwargs
        )

        self.fields[
            "resume"
        ].required = True

        self.fields[
            "cover_letter"
        ].required = True