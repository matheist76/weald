from django.shortcuts import render
from .models import Drives
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import DrivesAddForm

# Create your views here.
def index(request):
    return render(request, 'index.html')
def gm(request):
    return render(request, 'gm.html')
def player(request):
    return render(request, 'player.html')
def settings(request):
    return render(request, 'settings.html')
def main(request):
    return render(request, 'main.html')
def get_page(request, page):
    return render(request, page)
def drives(request):
    member = Drives.objects.all().values()
    template = loader.get_template('drives.html')
    context = {
        'member': member,
    }
    return HttpResponse(template.render(context, request))
def addrecord(request):
    x = request.POST['name']
    y = request.POST['description']
    member = Drives(name=x, description=y)
    member.save()
    return HttpResponseRedirect('/drives.html')

def add_drive(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DrivesAddForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a
            # new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DrivesAddForm()

    return render(request, 'drivesadd.html', {'form': form})