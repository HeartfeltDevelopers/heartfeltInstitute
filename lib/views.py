from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="coresms/login/")
def home(request):
    context = {}
    template = "lib/home.html"

    return render(request, template, context)
