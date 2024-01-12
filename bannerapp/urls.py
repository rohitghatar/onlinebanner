from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path
from bannerapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('banners/',views.banners, name='banners'),
    path('testimonial/',views.testimonial),
    path('profile/',views.profile, name='profile'),
    path('c_login/',views.c_login, name='c_login'),
    path('c_signup/',views.c_signup),
    path('p_login/',views.p_login, name='p_login'),
    path('p_signup/',views.p_signup),
    path('userlogout/',views.userlogout),
    path('deleteclient/<int:id>',views.deleteclient),
    path('deletepublisher/<int:id>',views.deletepublisher),
    path('upload_banner/',views.upload_banner, name='upload'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)