from django.shortcuts import render
from django.contrib.auth.models import User


def index(request): #When the first page run 1.
    username='guest' # 2. is filled as a  GUEST
    if request.user.is_authenticated: #we understand its already logged in (3.if logged in )
        username=request.user.username #4 Username takes from our data  puts in username
        
    request.session['user_name']=username   #5 in anycase the name is filled this way 
    context={
            'media_url':settings.MEDIA_URL,
            "imageName":'germany.png',
            
        }
    return render(request, 'mainApp/index.html',context)



