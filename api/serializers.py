from rest_framework import serializers

from accounts.models import User
from applications.models import Application
from jobs.models import Job


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "role",
        ]


class JobSerializer(serializers.ModelSerializer):

    recruiter = UserSerializer(
        read_only=True
    )

    class Meta:

        model = Job

        fields = [
            "id",
            "title",
            "company",
            "location",
            "salary",
            "description",
            "requirements",
            "skills",
            "job_type",
            "recruiter",
            "created_at",
        ]


class ApplicationSerializer(serializers.ModelSerializer):

    applicant = UserSerializer(
        read_only=True
    )

    job = JobSerializer(
        read_only=True
    )

    class Meta:

        model = Application

        fields = [
            "id",
            "job",
            "applicant",
            "resume",
            "cover_letter",
            "status",
            "applied_at",
            "updated_at",
        ]