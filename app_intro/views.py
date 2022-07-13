from django.shortcuts import render


from django.http import HttpResponse


# Create your views here.
def welcome(request):
    res = HttpResponse("Welcome to my project \n thank you")
    return res

def pro_1(request):
    return render(request,'home.html')

