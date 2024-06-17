from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("<h1>Internet site</h1> <img src='https://archive.unews.utah.edu/wp-content/uploads/2021/03/Cash.jpg'> Some description")

