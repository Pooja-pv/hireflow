from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render
)

from jobs.models import Job

from .forms import ApplicationForm
from .models import Application


@login_required
def apply_job(request, job_id):

    if request.user.role != "Applicant":

        messages.error(
            request,
            "Only applicants can apply for jobs."
        )

        return redirect(
            "job_detail",
            job_id=job_id
        )

    job = get_object_or_404(
        Job,
        id=job_id
    )

    existing = Application.objects.filter(
        job=job,
        applicant=request.user
    ).first()

    if existing:

        messages.info(
            request,
            "You have already applied for this job."
        )

        return redirect(
            "job_detail",
            job_id=job.id
        )

    if request.method == "POST":

        form = ApplicationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            application = form.save(
                commit=False
            )

            application.job = job

            application.applicant = (
                request.user
            )

            application.save()

            messages.success(
                request,
                "Application submitted successfully!"
            )

            return redirect(
                "my_applications"
            )

    else:

        form = ApplicationForm()

    return render(
        request,
        "applications/apply.html",
        {
            "form": form,
            "job": job
        }
    )


@login_required
def my_applications(request):

    applications = (
        Application.objects
        .filter(
            applicant=request.user
        )
        .select_related(
            "job"
        )
    )

    return render(
        request,
        "applications/my_applications.html",
        {
            "applications": applications
        }
    )


@login_required
def recruiter_applications(request):

    if request.user.role != "Recruiter":

        messages.error(
            request,
            "Only recruiters can access applications."
        )

        return redirect(
            "dashboard"
        )

    applications = (
        Application.objects
        .filter(
            job__recruiter=request.user
        )
        .select_related(
            "job",
            "applicant"
        )
    )

    return render(
        request,
        "applications/recruiter_applications.html",
        {
            "applications": applications
        }
    )


@login_required
def update_application_status(
    request,
    application_id
):

    if request.user.role != "Recruiter":

        messages.error(
            request,
            "Only recruiters can update applications."
        )

        return redirect(
            "dashboard"
        )

    application = get_object_or_404(
        Application,
        id=application_id,
        job__recruiter=request.user
    )

    if request.method == "POST":

        status = request.POST.get(
            "status"
        )

        valid_statuses = dict(
            Application.STATUS_CHOICES
        )

        if status in valid_statuses:

            application.status = status

            application.save()

            messages.success(
                request,
                "Application status updated."
            )

    return redirect(
        "recruiter_applications"
    )