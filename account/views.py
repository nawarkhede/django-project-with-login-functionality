from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from . import forms

# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = forms.Login(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(
                request,
                username=cleaned_data["username"],
                password=cleaned_data["password"],
            )
            if user and user.is_active:
                login(request, user)
                return redirect(reverse("dashboard"))
                # return HttpResponse("Loggedin")

            else:
                return redirect(reverse("login"))

    else:
        form = forms.Login()

    return render(request, "account/login.html", {"form": form})


@login_required
def dashboard(request):
    return render(request, "account/dashboard.html", {"section": "dashboard"})
