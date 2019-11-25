from django.shortcuts import render, redirect,render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from bokeh.plotting import figure,output_file,show
from bokeh.embed import components
from bokeh.palettes import Category20c
from bokeh.transform import cumsum
import random
import numpy as np
import pandas as pd
import bokeh
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, RangeTool
from bokeh.sampledata.stocks import AAPL

# Create your views here.

def graph(request,*args,**kwargs):
   
    dates = np.array(AAPL['date'], dtype=np.datetime64)
    source = ColumnDataSource(data=dict(date=dates, close=AAPL['adj_close']))

    p = figure(plot_height=300, plot_width=800, tools="xpan", toolbar_location=None,
            x_axis_type="datetime", x_axis_location="below",
            background_fill_color="#efefef", x_range=(dates[1500], dates[2500]))

    p.line('date', 'close', source=source)
    p.yaxis.axis_label = 'Price'

    #Store Components
    script,div = components(p)
    context = {'script':script,'div':div}
    return render_to_response('graph.html',context=context)
@login_required(login_url='login')
def dashboard(request,*args,**kwargs):
    dates = np.array(AAPL['date'], dtype=np.datetime64)
    source = ColumnDataSource(data=dict(date=dates, close=AAPL['adj_close']))

    p = figure(plot_height=300, plot_width=800, tools="xpan", toolbar_location=None,
            x_axis_type="datetime", x_axis_location="below",
            background_fill_color="#efefef", x_range=(dates[1500], dates[2500]))

    p.line('date', 'close', source=source)
    p.yaxis.axis_label = 'Price'

    #Store Components
    script,div = components(p)

    user = User.objects.get(username = request.user)
    context = {'user':user, 'script':script,'div':div}
    return render_to_response('dashboard.html',context)

@login_required(login_url='login')
def map(request, *arg, **kwargs):
    return render(request, 'map.html', {})

@login_required(login_url='login')
def notification(request, *arg, **kwargs):
    return render(request, 'notifications.html', {})

@login_required(login_url='login')
def user(request, *arg, **kwargs):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        user_form = UserProfileForm(request.POST)
        if user_form.is_valid():
            profile = UserProfile.objects.get_or_create(user=user,first_name=request.POST['first_name'],last_name=request.POST['last_name'],age=request.POST['age'],address=request.POST['address'],country=request.POST['country'],city=request.POST['city'],about_me=request.POST['about_me'])
            profile.save()

        else:
            return render(request = request,template_name = "login.html")
    else:
        try:   
            profile_form = UserProfileForm()                       
            profile = UserProfile.objects.get(user=request.user)
            context = {'form':profile_form,'profile':profile}
            return render(request, 'user.html', context=context)
        except Exception:
            profile_form = UserProfileForm()        
            context = {'form':profile_form}
            return render(request, 'user.html', context=context)
# def fuel_track(request,*args,**kwargs):
#     if request == 'POST':
#         fuel_track_form = FuelTrack(request.POST)
#         if fuel_track_form.is_valid:
#             fuel = FuelTrack(user=request.user,unit_price=request.POST['unit_price'],litter=request.POST['litter'],vendor=request.POST['vendor'])
#         return redirect('dashboard')
#     else:
#         track_fuel = fuel_track_form()
#         context = {'form':track_fuel}
#         return render(request=request,template_name='dashboard.html',context=context)
        