from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from home.models import Entry
# Create your views here.
def index(request):
    return HttpResponse('hi')
def home(request):
    return render(request,'home.html')
def show(request):

     data = Entry.objects.all()
     return render(request,"show.html",{'data':data})
    #return render(request,'show.html')
def send(request):
    if request.method == "POST":
        id1=request.POST['id1']
        id2=request.POST['id2']
        id3=request.POST['id3']
        send=Entry(id1=id1,id2=id2,id3=id3)
        send.save()
        msg="Data insert Successfully"
        return render(request,'home.html',{'msg':msg})
    else:
        return HttpResponse("filed")
def delete(request):
    id1=request.GET['id']
    Entry.objects.filter(id1=id1).delete()
    return HttpResponseRedirect("/show")
"""def edit(request):
    id1=request.GET['id']
    id2 = id3 = "Not Available"
    for data in Entry.objects.filter(id1,id1):
        id2=data.id2
        id3=data.id3
    return render(request,'edit.html',{'id1':id1,'id2':id2,'id3':id3})
def recordEdited(request):
    if request.method == 'POST':
        id1= request.POST['id1']
        id2 = request.POST['id2']
        id3 = request.POST['data2']
        Entry.objects.filter(id1=id1).update(id2=id2,id3=id3)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")"""

def edit(request):
    id1 = request.GET['id']
    id2 = id3 = "Not Available"
    for data in Entry.objects.filter(id1=id1):
        id2 = data.id2
        id3 = data.id3

    return render(request,"edit.html",{'id1':id2,'id2':id2,'id3':'id3'})

def recordEdited(request):
    if request.method == 'POST':
        id1 = request.POST['id1']
        id2= request.POST['id2']
        id3= request.POST['id3']
        Entry.objects.filter(id1=id1).update(id1=id1,id2=id2,id3=id3)
        return HttpResponseRedirect("/show")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")