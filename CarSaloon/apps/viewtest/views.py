from multiprocessing import context
from django.shortcuts import render
from django.views import View


def hello(request):
    
        context={
            'name':'Max Jokar and  Django:from View : def hello(request):'
            
        }
        return render(request,'viewtest/page0.html',context)
