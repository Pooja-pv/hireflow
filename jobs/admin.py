from django.contrib import admin

from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "company",
        "location",
        "salary",
        "job_type",
        "recruiter",
        "created_at",
    )

    search_fields = (
        "title",
        "company",
        "location",
        "skills",
    )

    list_filter = (
        "job_type",
        "location",
        "created_at",
    )