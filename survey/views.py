from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Choose


# Create your views here.
def login(request):
    return redirect("account_login")


@login_required(login_url="account_login")
def survey(request):

    if str(request.user) == "admin" and request.POST:
        # Return to admin dashboard
        return redirect("dashboard")

    # Return to survey qustions
    return render(request, "survey/index.html")


@login_required(login_url="account_login")
def add_servey(request):

    if request.POST:
        choose = dict(request.POST)
        choose.pop("csrfmiddlewaretoken")

        for q, a in choose.items():
            for userChoose in a:
                Choose.objects.create(question=q, answer=userChoose)

        return redirect("thanks")

    return redirect("survey")


@login_required(login_url="account_login")
def thanks(request):
    return render(request, "survey/thanks.html")
