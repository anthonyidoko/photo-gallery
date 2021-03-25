from django import forms
from .models import Category, Picture 

class UserPictureUpload(forms.ModelForm):
    
    class Meta:
        model = Picture
        fields = ['category',"image","description"]

        



class UserCategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=2000, widget=forms.TextInput(attrs={
        "placeholder": "Input Category", 'class': 'category'
    }))
    class Meta:
        model = Category
        fields = ["name"]
        
