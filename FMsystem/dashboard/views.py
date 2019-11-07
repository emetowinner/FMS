from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.
@login_required(login_url='login')
def dashboard(request,*args,**kwargs):
    user = User.objects.get(username = request.user)
    return render(request=request,template_name='dashboard.html',context = {'user':user})

@login_required(login_url='login')
def map(request, *arg, **kwargs):
    return render(request, 'map.html', {})

@login_required(login_url='login')
def notification(request, *arg, **kwargs):
    return render(request, 'notifications.html', {})

@login_required(login_url='login')
def user(request, *arg, **kwargs):
    user = User.objects.get(username = request.user)
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST)
        if user_form.is_valid():
            profile = UserProfile(user=user.username,profile_picture=request.POST['profile_picture'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],birth_date=request.POST['birth_date'],email=request.POST['email'],address=request.POST['address'],country=request.POST['country'],city=request.POST['city'],about_me=request.POST['about_me'])
            profile.save()
            return redirect('profile')

        else:
            return render(request = request,
                        template_name = "user.html",)
    else:
        profile_form = UserProfileForm()
        user = User.objects.get(username = request.user)
        context = {'form':profile_form,'user':user}
        return render(request, 'user.html', context=context)