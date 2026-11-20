# from django import forms
# from .models import Job


# class JobForm(forms.ModelForm):
#     class Meta:
#         model = Job
#         fields = [
#             "title",
#             "company",
#             "location",
#             "description",
#             "requirements",
#             "skills",
#             "job_type",
#             "salary",
#         ]

#         widgets = {
#             "title": forms.TextInput(attrs={
#                 "class": "form-control",
#                 "placeholder": "e.g. Python Developer",
#             }),
#             "company": forms.TextInput(attrs={
#                 "class": "form-control",
#                 "placeholder": "Company name",
#             }),
#             "location": forms.TextInput(attrs={
#                 "class": "form-control",
#                 "placeholder": "e.g. Bangalore / Remote",
#             }),
#             "description": forms.Textarea(attrs={
#                 "class": "form-control",
#                 "rows": 5,
#                 "placeholder": "Describe the job...",
#             }),
#             "requirements": forms.Textarea(attrs={
#                 "class": "form-control",
#                 "rows": 5,
#                 "placeholder": "Enter job requirements...",
#             }),
#             "skills": forms.TextInput(attrs={
#                 "class": "form-control",
#                 "placeholder": "Python, Django, MySQL, REST API",
#             }),
#             "job_type": forms.Select(attrs={
#                 "class": "form-control",
#             }),
#             "salary": forms.TextInput(attrs={
#                 "class": "form-control",
#                 "placeholder": "e.g. ₹5-8 LPA",
#             }),
#         }