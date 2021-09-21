from django import urls
from rest_framework import routers, urlpatterns, views,viewsets
from django.urls import path,include
from . import views

router=routers.DefaultRouter()

router.register(r'signin',views.loginviewsets)

 
urlpatterns=[
   path('',include(router.urls)),
   path('login/',views.signinview)
]