from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}')
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request,'users/register.html', {'form':form})

@login_required
def profilepage(request):
    user = request.user
    username = request.user.username
    email = request.user.email
    profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    if profile_form.is_valid():
        profile_form.save()
        messages.success(request, f'Your account has been updated!')

        return redirect('profile')
    else:
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'username' : username,
        'email' : email,
        'profile_form' : profile_form
    }


    return render(request, 'users/profile.html', context)


