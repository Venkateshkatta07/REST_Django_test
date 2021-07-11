from django.urls import path,include
from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello-viewset')

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view(),name='hello'),
    path('',include(router.urls)),
]
