from django.shortcuts import render
from .models import Test

# Create your views here.

def home(request):
    obj = Test.objects.all()
    return render(request, 'login.html', {'obj': obj})