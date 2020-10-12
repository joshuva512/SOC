from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from app import models



def home(request):
    return render(request, 'home.html')

@login_required
def user_base(request):
    return render(request, 'user_base.html')

def s1(request):
    video = models.COMPUTER_HARDWARE_SERVICING_AND_NETWORKING.objects.all()
    context = {'video':video}
    return render(request, 's1.html', context)

def s2(request):
    video = models.MICROCONTROLLER_AND_ANDROID_OS.objects.all()
    context = {"video":video}
    return render(request, 's2.html', context)

def s3(request):
    video = models.VLSI.objects.all()
    context = {"video":video}
    return render(request, 's3.html', context)

def s4(request):
    video = models.DIGITAL_COMMUNICATION.objects.all()
    context = {"video":video}
    return render(request, 's4.html', context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html',{'form':form})
