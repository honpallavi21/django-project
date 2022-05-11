from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm

def index(request):
    return render(request, 'static_app/index.html', {})

def registerUser(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegisterForm()
    return render(request, 'static_app/register.html', {'form':form})

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username or Password is Incorrect')
        else:
            messages.error(request, 'Fill out all the fields')

    return render(request, 'static_app/login.html', {})

def home(request):
    return render(request, 'static_app/home.html', {})


def logoutUser(request):
    logout(request)
    return redirect('index')


# Create your views here.
