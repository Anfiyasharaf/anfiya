from django.shortcuts import render
from django.http import HttpResponse
def tem(request):
    return  HttpResponse("hiiiiii")
def demo(request):
    return render (request,"index.html")
def demo2(request):
    return render (request,"contact.html")
def new(request):
    return render(request,"news.html")
#def addition(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #res=x+y
    #mul=x*y
    #div=x/y
    #sub=x-y
    #return render(request,"result.html",{'res':res,'mul':mul,'div1':div,'sub1':sub})
    
    
