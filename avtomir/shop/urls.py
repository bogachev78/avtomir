from django.urls import path
from .views import *


urlpatterns = [
    path('', shopIndex, name='shop_index'),
]