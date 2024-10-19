from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# Create your views here.

def index(request):
    RPSFRONT = Item.objects.all()
    context = {'rpsfront': RPSFRONT}
    return render(request, 'content.html',context )

def products(request):
    RPSFRONT = Item.objects.all()
    context = {'rpsfront': RPSFRONT}
    return render(request, 'products.html',context )

def search(request):

    if request.method == "POST":
        searched = request.POST['searched']
        products = Item.objects.filter(item_name__contains=searched)
        return render(request, 'search.html',{'searched':searched,'products':products})
    else:
        return render(request, "search.html")