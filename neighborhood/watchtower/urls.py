from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
urlpatterns=[
    url(r'^$',views.watch,name='watch'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^search/', views.search, name='search'),
    url(r'^post/', views.post, name='post'),
]
