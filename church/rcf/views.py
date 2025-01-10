from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import SigninForm, SignUpForm, CustomUserForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)  # Add request.FILES for handling file uploads
        if form.is_valid():
            user = form.save()  # Save the user
            login(request, user)  # Log the user in after registration
            return redirect('profile')  # Redirect to profile after successful signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            user = form.user  # Get the authenticated user from the form
            login(request, user)
            return redirect('profile')  # Redirect directly to profile page after sign-in
    else:
        form = SigninForm()
    return render(request, 'signin.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home after logout

@login_required
def market(request):
    return render(request, 'market.html')

def response(request):
    return render(request, 'response.html', {'message': 'Welcome! You are logged in.'})  # Optional message after sign-in

@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})

@login_required
def settings_view(request):
    """
    Allows the user to update their profile picture and bio.
    """
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')  # Redirect to profile page after update
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserForm(instance=request.user)

    return render(request, 'settings.html', {'form': form})
