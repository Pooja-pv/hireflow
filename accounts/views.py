from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import ProfileForm, RegisterForm


def register_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(
                request,
                "Account created successfully!"
            )

            return redirect("dashboard")

    else:

        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            login(
                request,
                form.get_user()
            )

            return redirect("dashboard")

    else:

        form = AuthenticationForm()

    return render(
        request,
        "accounts/login.html",
        {"form": form}
    )


@login_required
def logout_view(request):

    logout(request)

    messages.success(
        request,
        "You have been logged out."
    )

    return redirect("login")


@login_required
def profile_view(request):

    if request.method == "POST":

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Profile updated successfully!"
            )

            return redirect("profile")

    else:

        form = ProfileForm(
            instance=request.user
        )

    return render(
        request,
        "accounts/profile.html",
        {"form": form}
    )