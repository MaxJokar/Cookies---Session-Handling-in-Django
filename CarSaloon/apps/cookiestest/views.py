from django.shortcuts import render


def index(request):

    context={
         
    } 
    return render(request,"cookiestest/index.html",context)

#save name info save somewhere :

def set_cookies(request):
    response=render(request,"cookiestest/page1.html")
    response.set_cookie(key='name',value='Max',max_age=60) # To save a cookie #max_age:keeps our data till 60 Sec 
    response.set_cookie(key='family',value='jokar',max_age=60)   
    response.set_cookie(key='age',value='42',max_age=60)
    return response

# 1 .To return datas from our cookie we need the following function 
# def get_cookies(request):
#     name=request.COOKIES['name']
#     family=request.COOKIES['family']
#     age=request.COOKIES['age']
#     context={
#         'name':name,
#         'family':family,
#         'age':age,
#     }
#     return render(request, "cookiestest/page2.html",context)

#2:
def get_cookies(request):
    context={}
    if request.COOKIES.get('name'): #if you found fill them all with name , family age otherwise ,get the empty context :
        name=request.COOKIES['name']
        family=request.COOKIES['family']
        age=request.COOKIES['age']
        context={
            'name':name,
            'family':family,
            'age':age,
        }
        return render(request, "cookiestest/page2.html",context)














