from django.shortcuts import render
from .models import MakeForm

def index(request):
    thank = False
    if request.method == "POST":
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        index = MakeForm(first_name=first_name, email=email, last_name=last_name)
        index.save()
        thank = True
        return render(request, "index.html", {'thank': thank})

    return render(request, "index.html")

# Create your views here.
