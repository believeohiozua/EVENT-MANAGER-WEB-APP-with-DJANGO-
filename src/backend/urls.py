# accounts/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.homePage, name='home'),
    path('', views.workPage, name='work'),
    path('', views.servicesPage, name='services'),
    path('', views.contactPage, name='contact'),
    path('', views.aboutPage, name='about'),
]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)