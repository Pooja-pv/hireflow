from django.conf import settings
from django.db import models


class Job(models.Model):

    title = models.CharField(
        max_length=200
    )

    company = models.CharField(
        max_length=200
    )

    location = models.CharField(
        max_length=200
    )

    salary = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    description = models.TextField()

    requirements = models.TextField()

    skills = models.TextField()

    job_type = models.CharField(
        max_length=100
    )

    recruiter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posted_jobs"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title