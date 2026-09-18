from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render

from applications.models import Application
from jobs.models import Job


@login_required
def dashboard_view(request):

    if request.user.role == "Recruiter":

        jobs = Job.objects.filter(
            recruiter=request.user
        )

        applications = Application.objects.filter(
            job__recruiter=request.user
        )

        jobs_count = jobs.count()

        applications_count = applications.count()

        pending_count = applications.filter(
            status="Applied"
        ).count()

        shortlisted_count = applications.filter(
            status="Shortlisted"
        ).count()

        hired_count = applications.filter(
            status="Hired"
        ).count()

        return render(
            request,
            "dashboard/recruiter_dashboard.html",
            {
                "jobs_count": jobs_count,
                "applications_count":
                    applications_count,
                "pending_count":
                    pending_count,
                "shortlisted_count":
                    shortlisted_count,
                "hired_count":
                    hired_count,
            }
        )

    applications_count = Application.objects.filter(
        applicant=request.user
    ).count()

    return render(
        request,
        "dashboard/dashboard.html",
        {
            "applications_count":
                applications_count
        }
    )