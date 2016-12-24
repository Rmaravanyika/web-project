from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^mentor/', views.mentor, name='mentor'),
    url(r'^coding-clubs/', views.coding_clubs, name='coding_clubs'),
    url(r'^events/', views.events, name='events'),
    url(r'^social-impact/', views.social_impact, name='social_impact'),
    url(r'^donate/', views.donate, name='donate'),
    url(r'^contact/', views.contact, name='contact'),
    ]
