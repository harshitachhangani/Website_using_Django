from multiprocessing import context
from django.shortcuts import render, HttpResponse

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

def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("This is Contact Page")
    