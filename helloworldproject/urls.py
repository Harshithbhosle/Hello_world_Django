from django.urls import path
from helloworldapp.views import hello_world

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('hello/', hello_world, name='hello_world'),
]
