from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.watch,name='watch'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^search/', views.search, name='search'),
    url(r'^post/', views.post, name='post'),
    url(r'^viewpost/(\d+)', views.viewpost, name='viewpost'),
    url(r'^establishment/', views.establishment, name='establishment'),
    url(r'^viewestablishment/', views.viewestablishment, name='viewestablishment'),

]
