from django import forms
from .models import upload

class uploadform(forms.ModelForm):
    #image = forms.FileField(widget=forms.FileInput())
    class Meta():
        model = upload
        fields = ('image',)
