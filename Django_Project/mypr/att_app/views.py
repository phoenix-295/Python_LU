from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, MasterForm
from .models import Master_Data
from django.contrib import messages
# Create your views here.

posts = [
    {
        'name' : 'abc',
        'roll_no' : 20,
        'class' : "CSE"
    },
    {
        'name' : 'xyz',
        'roll_no' : 1,
        'class' : "CSE"
    }
]

def home(request):
    # return HttpResponse("<h1> Hello Everyone </h1>")
    c1 = {'data1' : posts, 'title' : 'Game Over'}
    return render(request, 'att_app/home.html', c1)


def about(request):
    return render(request, 'att_app/about.html')

def form_test(request):
	form =   ContactForm()
	context = {'form':form }
	return render (request,'att_app/display_form.html', context)

def master_data(request):
    form = MasterForm()
    context = {'form' : form}

    if request.method == 'POST':
        form1 = MasterForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('display-master')
    return render (request,'att_app/display_form.html', context)

def display_master(request):
	data = Master_Data.objects.all()
	context = {'data': data}
	return render (request,'att_app/display_data.html', context)