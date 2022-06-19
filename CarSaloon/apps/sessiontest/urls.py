from django.urls import path
import apps.sessiontest.views as views



urlpatterns = [
    path('',views.index),
    path('set/',views.set_session),
    path('get/',views.get_session),
    path('del/',views.delete_session),
    
    # path('setcookies/',views.set_cookies),
    # path('getcookies/',views.get_cookies),
    
    
]
