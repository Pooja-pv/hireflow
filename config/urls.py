from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import include, path


urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "",
        RedirectView.as_view(url="/login/", permanent=False),
        name="home"
    ),

    path(
        "",
        include("accounts.urls")
    ),

    path(
        "dashboard/",
        include("dashboard.urls")
    ),

    path(
        "jobs/",
        include("jobs.urls")
    ),

    path(
        "applications/",
        include("applications.urls")
    ),

    path(
        "api/",
        include("api.urls")
    ),
]


if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )