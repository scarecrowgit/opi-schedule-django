from django.urls import path
from .views import set_data, get_group

urlpatterns = [
    path('set_data/', set_data, name='set_data'),
    path('get_group/', get_group, name='get_group')
]
