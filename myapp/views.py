from django.shortcuts import render
from myapp.forms import TEXTTOHTMLFORM
# Create your views here.

def index(request):
    form=TEXTTOHTMLFORM()
    return render(request,'index.html',{'form':form})