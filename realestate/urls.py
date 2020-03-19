from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path
from app1.views import index,allproperty,details,about,contact,blog,blog_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('allproperty/',allproperty,name="property_list"),
    path('details/<id>/',details,name="property_detail"),
    path('about/',about),
    path('contact/',contact,name="contact_detail"),
    path('blog/',blog,name="blog"),
    path('blog_details/<id>/',blog_details,name="blog_details"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)