from django.test import TestCase
from django.urls import reverse

from accounts.models import User
from .models import Job


class JobTestCase(TestCase):

    def setUp(self):

        self.recruiter = User.objects.create_user(
            username="recruiter",
            password="testpass123",
            email="recruiter@test.com",
            role="Recruiter"
        )

        self.job = Job.objects.create(
            title="Python Developer",
            company="HireFlow Tech",
            location="Kochi",
            salary=600000,
            description="Python development",
            requirements="Django experience",
            skills="Python, Django",
            job_type="Full Time",
            recruiter=self.recruiter
        )

    def test_job_created(self):

        self.assertEqual(
            self.job.title,
            "Python Developer"
        )

    def test_job_list(self):

        self.client.login(
            username="recruiter",
            password="testpass123"
        )

        response = self.client.get(
            reverse("job_list")
        )

        self.assertEqual(
            response.status_code,
            200
        )