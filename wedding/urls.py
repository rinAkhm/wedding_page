from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_url, name='wedding_page'),
]
