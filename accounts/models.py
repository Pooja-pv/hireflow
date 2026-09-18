from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = [
        ("Applicant", "Applicant"),
        ("Recruiter", "Recruiter"),
    ]

    email = models.EmailField(unique=True)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="Applicant"
    )

    bio = models.TextField(
        blank=True
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    skills = models.TextField(
        blank=True,
        help_text="Enter skills separated by commas"
    )

    def __str__(self):
        return self.username