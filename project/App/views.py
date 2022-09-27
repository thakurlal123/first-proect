from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("this is home page")
    return render(request, 'Home.html')

def link(request):
    #return HttpResponse("this is link page")
    return render(request, 'link.html')

def Meetings(request):  
    #return HttpResponse("this is meetings page")
    return render(request, 'Meetings.html')