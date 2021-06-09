from django.shortcuts import render

def mainhomepage(request):
    return render(request,'mainhomepage.html')
