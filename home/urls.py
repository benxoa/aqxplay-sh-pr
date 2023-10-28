from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", home, name="home"),
    path("publish", publish, name="publish"),
    path("signup", signup, name="signup"),
    path("login", login, name="login"),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)