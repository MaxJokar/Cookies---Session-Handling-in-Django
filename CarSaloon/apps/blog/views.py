from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage 
from django.conf import settings
from .forms import *
from .models import *
from django.conf.urls.static import static
#  Create your views here.

def index(request):
    blogs=Blog.objects.all()
    context={
        "blogs":blogs,
        'media_url':settings.MEDIA_URL,     #DOest work , should fix it , Photoes dont come on Form 
    } 
    return render(request,"blog/index.html",context)
#=================================SEND EMAIL TO THE USERS=====send_mail==============================
#To send Email or  Email with Graphics :
# https://www.google.com/settings/security/lessecureapps

from django.core.mail import send_mail , EmailMultiAlternatives
# from django.conf import settings
#send email given below:
def sendEmail(subject,message,to): #Emails always include 3 info :to is a list!
    email_from=settings.EMAIL_HOST_USE     #sender  
    send_email(subject,message,email_from,to)
   
#=============================================EmailMultiAlternatives=================================
from django.core.mail import send_mail , EmailMultiAlternatives
from django.conf import settings
#send email given below: to send a content with html we should add "html_content" in our parameters 
def sendEmail2(subject,message,html_content,to): #Emails always include 3 info :to is a list!
    email_from=settings.EMAIL_HOST_USE     #sender  
    messgage=EmailMultiAlternatives(subject, message, email_from,to)
    message.attach_alternative(html_content,"text/html")
    message.send()
    send_email(subject,message,email_from,to)
   


def XXXXXXXXX(request):
    if request.method=="POST":
        form=BlogForm(request.POST) #==>request.FILES  is  Dictionary of  all file:
        if form.is_valid():
                data=form.cleaned_data
                blog=Blog() # from our model we create a instance
                blog.title=data['title']
                blog.description=data['description'] 
                blog.is_active=data['is_active']
                blog.save()
                return redirect(request,"blog/index.html")
                #return render(request,"blog/index.html") 
         
    else:
        form=BlogForm()
        context={
            'form': form, 
          
        }  
    return render(request, "blog/create.html",context)
             
    

#======================================================================================================
def create_blog2(request):
    if request.method=="POST":
        form=BlogForm(request.POST,request.FILES) #==>request.FILES  is  Dictionary of  all file:
        if form.is_valid():
            imageUpload=request.FILES['main_img']
            if imageUpload.size<1000000:
                if imageUpload.content_type=="image/jpeg" or imageUpload.content_type=="image/png":
                # if imageUpload.count_type=="image/jpeg" or imageUpload.count_type=="image/png" : 
                        #To avoid (dublicate Names or   changes in db with our Project )the Same Names we  Generate our name Prefix or suffix added to the Name:
                     
                    
                        # imagePath='images/blogimg/'+imageUpload.name
                        imagePath='images/blogimg/'+imageUpload.name
                       
                        #storage of data on the db:       blog=Blog (our model):    cleaned form=>(data)=form=BlogForm
                        data=form.cleaned_data
                        blog=Blog() # from our model we create a instance
                        blog.title=data['title']
                        blog.description= data['description']
                        blog.is_active=data['is_active'] 
                        blog.save()
                         #storage of data on Server
                        fss=FileSystemStorage()
                        # fss.save('images/blogimg/'+imageUpload.name, imageUpload)
                        fss.save(imagePath, imageUpload)
                        return render(request,"blog/index.html")
                    
                        # for(def sendEmail) sendEmail(" 2 Test Email our Article ","<h1>Article got successfully</h1>",['mmb2020max@gmail.com'])
                        # sendEmail2(" 3 Test Email our Article "," ","<h1>Article got successfully</h1>",['mmb2020max@gmail.com'])
                        #OR:
                      
                else:
                    context={ 'form':form,
                        'message':'Type OF File not GOOD'
                    }
                  
        
            else:
                context={
                    'form':form,
                    'message':'Size is bigger than 10 kilo byte'
                }
 
    else:
        form=BlogForm()
        context={
            'form':form,
        }
    return render(request,"blog/create.html",context)




















def create_blog3(request):
    if request.method=="POST":
        form=BlogForm(request.POST,request.FILES) #==>request.FILES  is  Dictionary of  all file:
        if form.is_valid():
            imageUpload=request.FILES['main_img']
            if imageUpload.size<1000000:
                if imageUpload.content_type=="image/jpeg" or imageUpload.content_type=="image/png":
                # if imageUpload.count_type=="image/jpeg" or imageUpload.count_type=="image/png" : 
                        #To avoid (dublicate Names or   changes in db with our Project )the Same Names we  Generate our name Prefix or suffix added to the Name:
                        import os 
                        import datetime
                        imgName,ext=os.path.splitext(imageUpload.name)
                        currenttime=datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
                    
                        # imagePath='images/blogimg/'+imageUpload.name
                        imagePath='images/blogimg/'+imgName+currenttime+ext
                       
                        #storage of data on the db:       blog=Blog (our model):    cleaned form=>(data)=form=BlogForm
                        data=form.cleaned_data
                        blog=Blog() # from our model we create a instance
                        blog.title=data['title']
                        blog.description= data['description']
                        blog.is_active=data['is_active']
                        blog.save()
                         #storage of data on Server
                        fss=FileSystemStorage()
                        # fss.save('images/blogimg/'+imageUpload.name, imageUpload)
                        fss.save(imagePath, imageUpload)
                        return render(request,"blog/index.html")
                    
                        # for(def sendEmail) sendEmail(" 2 Test Email our Article ","<h1>Article got successfully</h1>",['mmb2020max@gmail.com'])
                        # sendEmail2(" 3 Test Email our Article "," ","<h1>Article got successfully</h1>",['mmb2020max@gmail.com'])
                        #OR:
                        email_sub=" 3 Test Email our Article "
                        email_body="<h1 style='color:red'; >Article got successfully</h1>"
                        sendEmail2(email_sub," ",email_body,['mmb2020max@gmail.com'])
                else:
                    context={ 'form':form,
                        'message':'Type OF File not GOOD'
                    }
                  
        
            else:
                context={
                    'form':form,
                    'message':'Size is bigger than 10 kilo byte'
                }
 
    else:
        form=BlogForm()
        context={
            'form':form,
        }
    return render(request,"blog/create.html",context)






















