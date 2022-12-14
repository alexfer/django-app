from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            profile = Profile(user_id=user.id)
            profile.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account with username: %s has been created. You can now login.' % username,
                             extra_tags='alert alert-success')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)
        user_form = UserUpdateForm(request.POST, instance=request.user)

        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, f'Your profile has been updated!', extra_tags='alert alert-success')
            return redirect('profile')
    else:
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        user_form = UserUpdateForm(instance=request.user)

    return render(request, 'users/profile.html', {
        'profile_form': profile_form,
        'user_form': user_form,
    })
