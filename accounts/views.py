from django.shortcuts import render, redirect
from django.http import FileResponse, Http404
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import CreateUserForm,UploadForm
# from .filters import OrderFilter
# from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.

@login_required(login_url='login')
def home(request):
    #customers = Customer.objects.all()
    #context = {'customers': customers}

    #context = super().get_context_data(**kwargs)
    audios = Audio.objects.all()
    #context = {'audios':audios}
    #context['audios'] = audios
    return render(request, 'dashboard.html', dict(audios = Audio.objects.all()))


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for  ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)

# @login_required(login_url='login')
# def customer(request, pk):
#     customer = Customer.objects.get(id=pk)
#     audios = customer.audio_set.all()
#     context = {'customer': customer, 'audios': audios}
#
#     return render(request, 'customer.html', context)
#

@login_required(login_url='login')
def upload(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')

    return render(request, 'form.html', {'form': UploadForm})

@login_required(login_url='login')
def update_message(request,pk):
    message = Audio.objects.get(id=pk)
    form = UploadForm(instance=message)

    if request.POST:
        form = UploadForm(request.POST, instance=message)
        print(request.FILES)
        if form.is_valid():
            form.save()
        # return redirect(home)
    return render(request, 'form.html', {'form': UploadForm})

@login_required(login_url='login')
def play_audio(request,audio_id):
    audio = Audio.objects.get(pk=audio_id)
    if audio is not None:
        return render(request,'audio.html' , {'audio': audio})
    else:
        raise Http404('Audio Not Found')
    #return FileResponse(audio.audio_file.open())
