from django.shortcuts import render
from .models import Category, Picture
# Create your views here.

def home_view(request):
    categories = Category.objects.all()

    return render(request,"home.html",{"categories":categories})