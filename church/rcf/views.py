from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SigninForm, SignUpForm,CustomUser
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request,'index.html')
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)  # Add request.FILES for handling file uploads
        if form.is_valid():
            user = form.save()  # Save the user
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to home
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@csrf_exempt
def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            user = form.user  # Get the authenticated user from the form
            login(request, user)
            return redirect('response')  # Redirect to the response page after sign in
    else:
        form = SigninForm()
    return render(request, 'response.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home after logout


@login_required
def market(request):
    return render(request, 'market.html')


def response(request):
    return render(request, 'response.html')  # Render the response page after sign-in


@login_required
def profile_view(request):
    """
    Displays the profile page for the logged-in user.
    """
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
            return redirect('profile')
    else:
        form = CustomUserForm(instance=request.user)

    return render(request, 'settings.html', {'form': form})