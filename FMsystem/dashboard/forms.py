from django import forms

# Create your forms here.

class UserProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    age = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Age'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    address = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Home address'}))
    country = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nationality'}))
    city = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City/State'}))
    about_me = forms.CharField(max_length=300,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Bio'}))

class FuelTrackForm(forms.Form):
    user = forms.CharField(max_length = 100)
    unit_price = forms.IntegerField()
    litter = forms.IntegerField()
    vendor = forms.CharField(max_length = 100)
