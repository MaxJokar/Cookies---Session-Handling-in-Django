from django.urls import path
from .views import *




urlpatterns = [
     path('',index,name="blog_index"),
     # path('add/',create_blog,name="create_blog"),
     path('add2/',create_blog2,name="create_blog"),
      
     
]

#+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)