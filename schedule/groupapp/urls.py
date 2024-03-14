from django.urls import path
from .views import set_group, get_group

urlpatterns = [
    path('set_group/', set_group, name='set_group'),
    path('get_group/', get_group, name='get_group'),
]
