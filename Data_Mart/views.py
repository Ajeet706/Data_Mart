from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm 
from django.contrib import messages
from django.contrib.auth.models import User

def home_page(request):
    users = User.objects.all()  # Fetch all users
    return render(request, 'index.html', {'users': users})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            print(request.user)
            return render(request, 'index.html', {'user': request.user})
            # return redirect('HomePAge')  # Redirect to home or another page after login
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'registration/login.html')  # Display login form

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Save the user
            user = form.save()
            
            # Log the user in immediately after registration
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  # Correct field name
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

            # Redirect to a custom page after registration
            return redirect('HomePAge')  # Replace 'HomePage' with your desired redirect URL name
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def custom_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('HomePAge')  # Redirect to home or another page after logout