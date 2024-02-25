from django.shortcuts import render, redirect

from .models import Customer

from . forms import CreateUserForm, LoginForm, CustomerForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages

#-Authentication models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user,allowed_users,admin_only
def main_view(request):
    return render(request, 'authenticate/main.html',{})

@login_required(login_url='my_login')
def homepage(request):

    return render(request, 'authenticate/index.html')
@unauthenticated_user
def register(request):

    # form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)   

        if form.is_valid():
            
            user=form.save()
            username = form.cleaned_data.get('username')

            
            

            messages.success(request,'account was created for ' + username)
            return redirect("my_login")
    form = CreateUserForm()

    context = {'Form':form}

    return render(request, 'authenticate/register.html', context=context)
def userPage(request):
    context = {}
    return render(request, 'authenticate/name.html', context)

@login_required(login_url='my_login')
# @allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance= customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES,instance= customer)
        if form.is_valid():
            form.save()

        
    context={'form':form}
    return render(request, 'authenticate/account_setting.html',context)

@unauthenticated_user
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

                return redirect("user")
            else:
                # messages.info(request,'username Or password is incorect')

                messages.success(request, "Username or Password is incorect")
                
    context = {'Form':form}


    return render(request, 'authenticate/my_login.html', context=context)



@login_required(login_url="my_login")
def dashboard(request):

    return render(request, 'authenticate/dashboard.html')

def my_logout(request):
    logout(request)
    return redirect('my_login')