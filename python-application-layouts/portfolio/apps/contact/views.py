from django.shortcuts import render


def index(request):
    return render(request, "base.html", {"title": "Contact"})
