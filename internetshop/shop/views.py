from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    products = []
    return render(request, "index.html", {
        'products': products
    })

