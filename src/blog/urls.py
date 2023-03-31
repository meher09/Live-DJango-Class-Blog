from django.urls import path, include
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api', PostViewSet)



urlpatterns = [
    path('',home, name = 'home'),
    path('<slug:post_slug>', post_details, name = 'post_details'),
    path('category/<slug:category_slug>/',category_details, name = 'category_details'),
    path('', include(router.urls))
    
]

handler404 = handler404