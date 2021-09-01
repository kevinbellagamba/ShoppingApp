from ShoppingApp.models import Purchase
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    purchases = Purchase.objects.all()
    context = {
        'purchases' : purchases,
    }
    return render(request, 'index.html', context)