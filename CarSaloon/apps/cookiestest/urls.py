from django.urls import path
import apps.cookiestest.views as views



urlpatterns = [
    path('',views.index),
    path('setcookies/',views.set_cookies),
    path('getcookies/',views.get_cookies),
    
    
]
