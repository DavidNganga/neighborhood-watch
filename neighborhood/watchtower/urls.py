from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',views.watch,name='watch'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^search/', views.search, name='search'),
    url(r'^post/', views.post, name='post'),
    url(r'^viewpost/', views.viewpost, name='viewpost'),
    url(r'^viewprofile/', views.viewprofile, name='viewprofile'),
    url(r'^establishment/', views.establishment, name='establishment'),
    url(r'^profiledetails/(?P<id>\d+)', views.profiledetails, name='profiledetails'),
    url(r'^viewestablishment/', views.viewestablishment, name='viewestablishment'),
    url(r'^neighbourhoodprofile/', views.create_neighbourhood, name='neighbourhoodprofile'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
