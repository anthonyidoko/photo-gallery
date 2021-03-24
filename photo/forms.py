from django import forms
from .models import Category, Picture 

class UserPictureUpload(forms.ModelForm):

    class Meta:
        model = Picture
        fields = ['category',"image","description"]


class UserCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        
