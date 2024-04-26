from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from survey.models import Choose
from django.db.models import Count

# Create your views here.


@login_required(login_url="account_login")
def index(request):
    if str(request.user) == "admin":
        # Get all answers and count duplicated 
        q1 = (
            Choose.objects.filter(question="Q1")
            .values("answer")
            .annotate(count=Count("answer"))
        )
        q2 = (
            Choose.objects.filter(question="Q2")
            .values("answer")
            .annotate(count=Count("answer"))
        )
        q3 = (
            Choose.objects.filter(question="Q3")
            .values("answer")
            .annotate(count=Count("answer"))
        )
        q4 = (
            Choose.objects.filter(question="Q4")
            .values("answer")
            .annotate(count=Count("answer"))
        )

        context = {
            "q1": q1,
            "q2": q2,
            "q3": q3,
            "q4": q4,
        }

        return render(request, "dashboard/index.html", context)

    return redirect("survey")
