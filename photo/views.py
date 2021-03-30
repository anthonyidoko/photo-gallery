from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Category, Picture
from .forms import UserPictureUpload,UserCategoryForm
# Create your views here.
def create_category_view(request):
    form = UserCategoryForm()
    if request.method == "POST":
        form = UserCategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,"category created")
            return redirect("/")
    else:
        return render(request,'create_category.html',{"form":form})

def home_view(request):
    categories = Category.objects.all()
    if request.method == "POST":
        new = Category.objects.create()
        context = {"categories": categories, "new": new}

    context = {"categories": categories}
    return render(request,"home.html",context)

def all_photos_view(request):
    all_pictures = Picture.objects.all()
    return render(request, "all_photos.html", {"all_pictures": all_pictures})

    
def photos_view(request,pk):
    category = Category.objects.get(id=pk)
    pictures = Picture.objects.filter(category = category)
    context = {
        "category":category,
        'pictures':pictures
    }

    return render(request, "photos.html", context)

def user_form_view(request):
    if request.method == "POST":
        form = UserPictureUpload(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,"successfully saved")
            return redirect(".")
        else:
            messages.info(request,"invalid entry")
            UserPictureUpload()
    else:
        form = UserPictureUpload
        return render(request, "form.html", {'form': form})
