from django.conf import settings
from django.db import models

from jobs.models import Job


class Application(models.Model):

    STATUS_CHOICES = [

        ("Applied", "Applied"),

        ("Reviewing", "Reviewing"),

        ("Shortlisted", "Shortlisted"),

        ("Interview", "Interview"),

        ("Rejected", "Rejected"),

        ("Hired", "Hired"),
    ]

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    applicant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    resume = models.FileField(
        upload_to="resumes/",
        blank=True,
        null=True
    )

    cover_letter = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Applied"
    )

    applied_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        unique_together = (
            "job",
            "applicant"
        )

        ordering = [
            "-applied_at"
        ]

    def __str__(self):

        return (
            f"{self.applicant.username} - "
            f"{self.job.title}"
        )