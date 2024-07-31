from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, "index.html")


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Process the form data and create a new user
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['full_name']
            user.save()

            return redirect('user_login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data.get('remember_me')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                if remember_me:
                    request.session.set_expiry(1209600)  # for 2 weeks
                else:
                    request.session.set_expiry(0) # browser session
                return redirect('dashboard') 
            else:
                # Invalid login
                return render(request, 'login.html', {'form': form, 'invalid_login': True})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def user_logout(request):
    logout(request)
    return redirect('user_login')

