from django.shortcuts import render
from .models import Item

def index(request):
    items = Item.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'index.html', context)

def bags(request):
    items = Item.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'bags.html', context)

def bag(request, pk):
    items = Item.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'bags.html', context)