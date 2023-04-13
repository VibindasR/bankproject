from django.http import HttpResponse
from django.shortcuts import render
from . models import district
from . models import branch
# Create your views here.
def Branch(request):
    obj=district.objects.all()
    obj1=branch.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
def demo1(request):
    obj1=branch.objects.all()
    return render(request,"index.html",{'result':obj1})
