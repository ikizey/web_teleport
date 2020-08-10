from django.urls import path
from .views import home, teleport, create_url

urlpatterns = [
    path('', home, name="home"),
    path('create', create_url, name='create_url'),
    path('<str:url>', teleport, name="teleport"),
]
