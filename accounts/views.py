from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import CreateUserForm
# from .filters import OrderFilter
# from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.
def home(request):
    customers = Customer.objects.all()
    context = {'customers':customers}
    return render(request, 'dashboard.html',context)


def loginPage(request):
    
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'login.html', context)


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for  '+ user)
            return redirect('login')



    context = {'form':form}
    return render(request, 'register.html',context)


