from django.urls import path
from .views import (home_view, photos_view, 
                    user_form_view, create_category_view, all_photos_view)


urlpatterns = [
    path('', home_view, name = "home"),
    path("photos/<int:pk>/", photos_view,name = "photos"),
    path('userform/', user_form_view, name = "userform"),
    path("create_category/",create_category_view,name="category"),
    path("all_photos/", all_photos_view, name = "all_photos")
]
