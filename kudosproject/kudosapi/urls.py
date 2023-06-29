from django.urls import path, include
from rest_framework import routers
from kudosapi import views


router=routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'kudos', views.KudosViewSet)

urlpatterns = [
    path('', include(router.urls))
] 