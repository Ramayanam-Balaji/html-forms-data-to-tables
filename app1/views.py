from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *
# Create your views here.
def form(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        print(username)
        print(password)
        return HttpResponse('data is submitted')
    return render(request,'form.html')
def table(request):
    if request.method=='POST':
        topic=request.POST['tn']
        t1=Topic.objects.get_or_create(Topic_Name=topic)[0]
        t1.save()
        return HttpResponse('data is inserted')
    return render(request,'table.html')