from django.urls import path
from .views import home_view, photos_view


urlpatterns = [
    path('', home_view, name = "home"),
    path("photos/<int:pk>/", photos_view,name = "photos")
]
