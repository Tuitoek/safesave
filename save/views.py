from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.models import User


# Create your views here.
def landing(request):
    return render(request,'landing.html')

def home(request):
    return render(request,'home.html')

def wallet(request):
    finance = Finance.objects.all()
    savings = SavingPlan.objects.all()
    months = Month.objects.all()
    return render(request,'wallet.html',{"finance":finance,"savings":savings,"months":months})

def savings(request):
    savings = SavingPlan.objects.all()
    return render(request,'savings.html',{"savings":savings})

def addsave(request):
    form = SavingsForm()
    if request.method == "POST":
       form = SavingsForm(request.POST)
       if form.is_valid():
          form.save()
          return render(request,'savings.html')

       else:
            form = SavingsForm(request.POST)
    return render(request,"addsave.html",{"form":form})

def finance(request):
    form =FinanceForm()
    if request.method == "POST":
       form = FinanceForm(request.POST)
       if form.is_valid():
          form.save()
          return render(request,'savings.html')

       else:
            form = FinanceForm(request.POST)
    return render(request,'finance.html',{"form":form})
