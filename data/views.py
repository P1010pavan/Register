from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
# Create your views here.
def index1(request):
    if request.method == 'POST':
        form = Regist(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = Regist()
    return render(request,'regis.html/',{'form':form})
