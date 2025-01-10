from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SigninForm, SignUpForm
from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'index.html')

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')  # Redirect to the signin page upon successful signup
    else:
        form = SignUpForm()  # Display empty form initially
    return render(request, 'signup.html', {'form': form})

@csrf_exempt
def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)  # Pass only request.POST, not 'request' and 'data'
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to home page after sign-in
    else:
        form = SigninForm()  # Display the empty signin form initially
    return render(request, 'response.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home or login page after logout

def market(request):
    return render(request, 'market.html')