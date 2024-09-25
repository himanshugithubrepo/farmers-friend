from django.urls import path
from .views import RegisterFarmer

urlpatterns = [
    path('users/register/', RegisterFarmer.as_view(), name='RegisterFarmer'),
]
