from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #takes from main urls and matches to what page it forwards too
    path('blog/', views.home, name='blog-home'),
    path('about/', views.about, name='about-home'),
]