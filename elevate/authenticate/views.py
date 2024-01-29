from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages

#-Authentication models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

def homepage(request):

    return render(request, 'authenticate/index.html')

def register(request):

    # form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)   

        if form.is_valid():
            
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'account was created for' + user)
            return redirect("my_login")
    form = CreateUserForm()

    context = {'Form':form}

    return render(request, 'authenticate/register.html', context=context)

def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)


            if user is not None:

                auth.login(request,user)

                return redirect("dashboard")
            else:
                # messages.info(request,'username Or password is incorect')

                messages.success(request, "Username or Password is incorect")
                
    context = {'Form':form}


    return render(request, 'authenticate/my_login.html', context=context)

@login_required(login_url="my_login")
def dashboard(request):

    return render(request, 'authenticate/dashboard.html')

def user_logout(request):

    auth.logout(request)

    return redirect("")