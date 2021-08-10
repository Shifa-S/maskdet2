"""from django.urls import path
from  . import views
urlpatterns = [
    path('mask/',views.VideoCamera()),
]
"""
from django.urls import path
from  . views import * 
from maskapp import views

urlpatterns = [
    path('',livefe),
    path('mask_feed', views.mask(), name='mask'),
]



