from django import forms
from .models import Recommendation
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class RecommendationForm(forms.ModelForm):
    
    class Meta:
        model = Recommendation
        fields = ("first_name","last_name","job","relationship",
        "comment")

class CustomLoginForm(AuthenticationForm):
    class Meta: 
        model = User
        fiels = ['username','password']

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        username = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder':'Username', 'id':'username'}))
        password = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder':'Password', 'id':'password'}))
        self.fields['username'].label = False
        self.fields['password'].label = False    
