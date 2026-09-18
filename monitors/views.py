# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from monitors.form import MonitorForm


@login_required
def index(request):
    monitors = request.user.monitors.all().order_by("name")
    return render(request, "monitors/index.html", {"monitors": monitors})


@login_required
def create(request):
    if request.method == "POST":
        form = MonitorForm(request.POST)

        if form.is_valid():
            monitor = form.save(commit=False)

            monitor.user = request.user

            monitor.save()

            return redirect("monitors:index")
    else:
        form = MonitorForm()

    return render(
        request,
        "monitors/new.html",
        {
            "form": form,
        },
    )
