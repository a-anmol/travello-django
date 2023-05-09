from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def rslt(request):
    v1=request.GET["num1"]
    # post
    v2=request.GET["num2"]
    rlt= int(v1)+int(v2)
    return render(request, 'rslt.html',{'rslt':rlt})