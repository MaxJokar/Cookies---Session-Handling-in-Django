from django.urls import path
# import apps.formtest.views as views
from apps.viewtest.views import *


urlpatterns = [

    # path('index/',views.index,name="post_index"), #name helps  Reverse to get and give the url after get name 
    path('view0/',hello),
    #  path('view1/',ViewClass1.as_view(),name="viewClass1"),#when we access to a generic class as view 
    # path('add/',PostCreate.as_view(),name="viewClass1"),
    
]