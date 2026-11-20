from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from applications.models import Application
from jobs.models import Job

from .serializers import (
    ApplicationSerializer,
    JobSerializer
)


class JobListAPIView(
    generics.ListCreateAPIView
):

    serializer_class = JobSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):

        return Job.objects.all().order_by(
            "-created_at"
        )

    def perform_create(self, serializer):

        serializer.save(
            recruiter=self.request.user
        )


class JobDetailAPIView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = JobSerializer

    permission_classes = [
        IsAuthenticated
    ]

    queryset = Job.objects.all()


class ApplicationListAPIView(
    generics.ListCreateAPIView
):

    serializer_class = ApplicationSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):

        if self.request.user.role == "Recruiter":

            return Application.objects.filter(
                job__recruiter=self.request.user
            )

        return Application.objects.filter(
            applicant=self.request.user
        )

    def perform_create(self, serializer):

        serializer.save(
            applicant=self.request.user
        )


class ApplicationDetailAPIView(
    generics.RetrieveUpdateAPIView
):

    serializer_class = ApplicationSerializer

    permission_classes = [
        IsAuthenticated
    ]

    queryset = Application.objects.all()