from multiprocessing import context
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable1":"Harshita",
        "variable2":"Chhangani"
    }
    #return HttpResponse("This is Homepage....")
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is About Page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is Services Page")

def explore(request):
    return render(request, 'explore.html')
    #return HttpResponse("This is Services Page")

def risk(request):
    return render(request, 'risk.html')
    #return HttpResponse("This is risk Page")

def hazard(request):
    return render(request, 'hazard.html')
    #return HttpResponse("This is hazard Page")

def genelab(request):
    return render(request, 'genelab.html')
    #return HttpResponse("This is GeneLab Page")

def space_bio_pro(request):
    return render(request, 'space_bio_pro.html')
    #return HttpResponse("This is GeneLab Page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobno = request.POST.get('mobno')
        desc = request.POST.get('desc')
        contact = Contact(name=name , email=email, mobno=mobno, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been Sent !')
        
    return render(request, 'contact.html')
    #return HttpResponse("This is Contact Page")
    