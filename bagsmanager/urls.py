from django.urls import path
from .views import bags, index, bag

urlpatterns = [
    path('', index, name='index'),
    path('bags', bags, name='bags'),
    path('bag/<int:pk>', bag, name='bag'),
]