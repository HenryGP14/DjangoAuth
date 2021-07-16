from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required
def vwHome(request):
    return render(request, "index.html")


def vwLogin(request):
    return render(request, "login.html")

