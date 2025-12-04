from django.shortcuts import render
from django.contrib import messages
import string as s
import random as r



def select(request):
    return render(request,'select.html')

def succ(request):
    cat=request.POST.get('cat')
    lion=request.POST.get('lion')
    tiger=request.POST.get('tiger')
    
    if(cat and not tiger and not lion):
        messages="correct!!"
    elif(tiger and not cat and not lion):
        messages="correct"
    elif(lion and not cat and not tiger):
        messages="correct"    

    else:
        messages="Wrong!!"
        
        
        
    context={'ans':messages}
    return render(request,'succ.html',context) 


def otpp(request):
    a=s.digits
    b=s.ascii_letters
    c=r.sample(3,a)
    d=list(c)
    f=r.sample(3,b)
    g=list(f)
    h=d+g
    context={'ans':h}
    return render(request,'otpp.html',context)
    
    
    
    
    
   
            
