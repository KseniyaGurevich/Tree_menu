from django.shortcuts import render
from .models import MenuItem


def index(request):
    template = 'index.html'
    item_list = MenuItem.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, template, context)