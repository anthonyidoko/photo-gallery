from django.shortcuts import render
from .models import Category, Picture
from .forms import UserPictureUpload,UserCategoryForm
# Create your views here.

def home_view(request):
    categories = Category.objects.all()

    return render(request,"home.html",{"categories":categories})


def photos_view(request,pk):
    category = Category.objects.get(id=pk)
    pictures = Picture.objects.filter(category = category)
    context = {
        "category":category,
        'pictures':pictures
    }

    return render(request, "photos.html", context)

def user_form_view(request):
    form = UserPictureUpload
    form2 = UserCategoryForm
    return render(request, "form.html", {'form': form, 'form2': form2})
