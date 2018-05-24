from django.conf.urls import url,include
from . import views

urlpatterns=[
    url(r'^',views.watch,name='watch'),
    url(r'^profile/', views.profile, name='profile'),
]
