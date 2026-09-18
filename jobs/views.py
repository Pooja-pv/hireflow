from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render
)

from .models import Job


@login_required
def job_list(request):

    query = request.GET.get(
        "q",
        ""
    ).strip()

    location = request.GET.get(
        "location",
        ""
    ).strip()

    job_type = request.GET.get(
        "job_type",
        ""
    ).strip()

    jobs = Job.objects.all()

    if query:

        jobs = jobs.filter(
            Q(title__icontains=query)
            | Q(company__icontains=query)
            | Q(skills__icontains=query)
            | Q(description__icontains=query)
            | Q(requirements__icontains=query)
        )

    if location:

        jobs = jobs.filter(
            location__icontains=location
        )

    if job_type:

        jobs = jobs.filter(
            job_type__icontains=job_type
        )

    jobs = jobs.order_by(
        "-created_at"
    )

    paginator = Paginator(
        jobs,
        6
    )

    page_number = request.GET.get(
        "page"
    )

    page_obj = paginator.get_page(
        page_number
    )

    return render(
        request,
        "jobs/job_list.html",
        {
            "jobs": page_obj,
            "page_obj": page_obj,
            "query": query,
            "location": location,
            "job_type": job_type,
        }
    )


@login_required
def job_detail(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id
    )

    already_applied = False

    if request.user.role == "Applicant":

        already_applied = (
            job.applications
            .filter(
                applicant=request.user
            )
            .exists()
        )

    return render(
        request,
        "jobs/job_detail.html",
        {
            "job": job,
            "already_applied":
                already_applied,
        }
    )


@login_required
def create_job(request):

    if request.user.role != "Recruiter":

        messages.error(
            request,
            "Only recruiters can post jobs."
        )

        return redirect("dashboard")

    if request.method == "POST":

        salary = request.POST.get(
            "salary"
        )

        if not salary:

            messages.error(
                request,
                "Salary is required."
            )

            return render(
                request,
                "jobs/create_job.html"
            )

        Job.objects.create(

            title=request.POST.get(
                "title"
            ),

            company=request.POST.get(
                "company"
            ),

            location=request.POST.get(
                "location"
            ),

            salary=salary,

            description=request.POST.get(
                "description"
            ),

            requirements=request.POST.get(
                "requirements"
            ),

            skills=request.POST.get(
                "skills"
            ),

            job_type=request.POST.get(
                "job_type"
            ),

            recruiter=request.user,
        )

        messages.success(
            request,
            "Job posted successfully!"
        )

        return redirect("my_jobs")

    return render(
        request,
        "jobs/create_job.html"
    )


@login_required
def my_jobs(request):

    if request.user.role != "Recruiter":

        return redirect("dashboard")

    jobs = Job.objects.filter(
        recruiter=request.user
    ).order_by(
        "-created_at"
    )

    return render(
        request,
        "jobs/my_jobs.html",
        {"jobs": jobs}
    )


@login_required
def edit_job(request, job_id):

    if request.user.role != "Recruiter":

        return redirect("dashboard")

    job = get_object_or_404(
        Job,
        id=job_id,
        recruiter=request.user
    )

    if request.method == "POST":

        job.title = request.POST.get(
            "title"
        )

        job.company = request.POST.get(
            "company"
        )

        job.location = request.POST.get(
            "location"
        )

        job.salary = request.POST.get(
            "salary"
        )

        job.job_type = request.POST.get(
            "job_type"
        )

        job.skills = request.POST.get(
            "skills"
        )

        job.requirements = request.POST.get(
            "requirements"
        )

        job.description = request.POST.get(
            "description"
        )

        job.save()

        messages.success(
            request,
            "Job updated successfully!"
        )

        return redirect("my_jobs")

    return render(
        request,
        "jobs/edit_job.html",
        {"job": job}
    )


@login_required
def delete_job(request, job_id):

    if request.user.role != "Recruiter":

        return redirect("dashboard")

    job = get_object_or_404(
        Job,
        id=job_id,
        recruiter=request.user
    )

    if request.method == "POST":

        job.delete()

        messages.success(
            request,
            "Job deleted successfully!"
        )

        return redirect("my_jobs")

    return render(
        request,
        "jobs/delete_job.html",
        {"job": job}
    )