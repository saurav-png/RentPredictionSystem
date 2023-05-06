from django.shortcuts import render

def home(request):
    return render(request,'prediction/index.html')

def result(request):

    return render(request,'prediction/index.html')