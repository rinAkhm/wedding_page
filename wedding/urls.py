from django.urls import path
from . import views

urlpatterns = [
    path('', views.wedding_form, name='wedding_page'),
    path('', views.base_url, name='wedding_page'),
    path('create/', views.wedding_form),
]
