from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .form import MeterReadingForm
from .models import MeterReading 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views import View

def home(request):
    return render(request,'base/home.html',{})





@login_required
def meter_input(request):
    if request.method == 'POST':
        form = MeterReadingForm(request.POST)
        if form.is_valid():
            reading = form.save(commit=False)
            reading.user = request.user
            reading.save()
            return redirect('meter_input')
    else:
        form = MeterReadingForm()

    readings = MeterReading.objects.filter(user=request.user).order_by('-timestamp')
    
    return render(request, 'base/meter_input.html', {'form': form, 'readings': readings})


class SignUpView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'base/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'base/signup.html', {'form': form})