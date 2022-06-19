from django.shortcuts import render


def index(request):

    context={
         
    } 
    return render(request,"sessiontest/index.html",context)
    
    
   #1.we set and fill the session ! 
def set_session(request):
    request.session['email']='m.maxjokar@gmail.com'
    request.session['password']="123456789"
    return render(request, "sessiontest/page1.html")
    
   #2.We get the information or datas  
def get_session(request):
    context={} #after set,get,del,del then if we get it brings empty Context!
    if 'email' in request.session: #we add this part to check if it doesnt exist we wont have error
        email=request.session['email']
        password=request.session['password']
        context={
            'password':password, 
            'email':email,
        
        }
    return render(request, "sessiontest/page2.html",context)

def delete_session(request):
    flag=False
    if 'email' in request.session:
        del request.session['email']
        del request.session['password']
        flag=True
        
    return render(request,"sessiontest/page3.html",{'flag':flag})    
        
################A Project######################################    
        