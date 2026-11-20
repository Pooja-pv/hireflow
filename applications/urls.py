from django.urls import path

from . import views


urlpatterns = [

    path(
        "apply/<int:job_id>/",
        views.apply_job,
        name="apply_job"
    ),

    path(
        "my/",
        views.my_applications,
        name="my_applications"
    ),

    path(
        "recruiter/",
        views.recruiter_applications,
        name="recruiter_applications"
    ),

    path(
        "<int:application_id>/status/",
        views.update_application_status,
        name="update_application_status"
    ),
]