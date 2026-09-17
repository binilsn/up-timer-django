# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    monitors = request.user.monitors.all().order_by("name")
    return render(request, "monitors/index.html", {"monitors": monitors})
