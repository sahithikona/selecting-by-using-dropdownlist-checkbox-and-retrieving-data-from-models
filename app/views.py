from django.shortcuts import render
# Create your views here.
from app.models import *

def insert_webpage(request):

    lto=topic.objects.all()
    d={"lto":lto}
    if request.method=="POST":
        tn=request.POST["tn"]
        nam=request.POST["na"]
        ur=request.POST["ur"]

        t=topic.objects.get(topic_name=tn)
        wo=webpage.objects.get_or_create(topic_name=t,name=nam,url=ur)[0]
        wo.save()

        qsw=webpage.objects.all()
        d1={"qsw":qsw}
        return render(request,"display_webpage.html",d1)
    
    return render(request,"insert_webpage.html",d)

def select_and_display(request):
    lto=topic.objects.all()
    d={"lto":lto}
    if request.method=="POST":
        tnl=request.POST.getlist("tn")
        qsw=webpage.objects.none()
        for ob in tnl:
            qsw=qsw | webpage.objects.filter(topic_name=ob)
        dict={"qsw":qsw}
        return render(request,"display_webpage.html",dict)

    return render(request,"select_and_display.html",d)


def checkbox(request):
    tol=topic.objects.all()
    dict1={"tol":tol}
    return render(request,"checkbox.html",dict1)




