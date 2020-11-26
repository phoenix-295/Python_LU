from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Att_Home"),
    path('about', views.about, name="About"),
    path('contact',views.form_test, name="Contact"),
    path('master', views.master_data, name='att-masterdata'),
    path('dismaster', views.display_master, name='display-master')
]
