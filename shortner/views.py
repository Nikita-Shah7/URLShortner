from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'index.html')


def create(request):    
    # print(request)
    if request.method == 'POST':
        # print("nik")
        link = request.POST.get('link')
        id = str(uuid.uuid4())[:7]
        # print(uuid)
        newUrl = Url(link=link,uuid=id)
        newUrl.save()
    return render(request,'index.html',{'link':link, 'uuid':id})


def visit(request,nik):
    url_details = Url.objects.get(uuid=nik) # get object that has uuid=nik
    return redirect(url_details.link)