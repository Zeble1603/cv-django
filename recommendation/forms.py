from django import forms
from .models import Recommendation


class RecommendationForm(forms.ModelForm):
    
    class Meta:
        model = Recommendation
        fields = ("first_name","last_name",
                  "job","relationship","comment")

  
