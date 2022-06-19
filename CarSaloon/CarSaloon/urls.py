
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.mainApp.urls'),name='mainapp'),
    path('post/',include('apps.viewtest.urls'),name='post'),
    path('blog/',include('apps.blog.urls')),
    path('cookiestest/',include('apps.cookiestest.urls'),name='redirect'),
    path('sessiontest/',include('apps.sessiontest.urls'),name='redirect'),

    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




 
 
 
 
 
 
  