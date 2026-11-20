from django.urls import path

from .views import (
    ApplicationDetailAPIView,
    ApplicationListAPIView,
    JobDetailAPIView,
    JobListAPIView,
)


urlpatterns = [

    path(
        "jobs/",
        JobListAPIView.as_view(),
        name="api_jobs"
    ),

    path(
        "jobs/<int:pk>/",
        JobDetailAPIView.as_view(),
        name="api_job_detail"
    ),

    path(
        "applications/",
        ApplicationListAPIView.as_view(),
        name="api_applications"
    ),

    path(
        "applications/<int:pk>/",
        ApplicationDetailAPIView.as_view(),
        name="api_application_detail"
    ),
]