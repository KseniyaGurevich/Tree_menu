from django.shortcuts import render, get_object_or_404
from .models import MenuItem


def item_detail(request, url):
    item = get_object_or_404(MenuItem, url=url)
    item.is_active = True
    item.save()
    template = 'menu.html'
    context = {
        'item': item,
    }
    return render(request, template, context)


def index(request):
    template = 'index.html'
    item_list = MenuItem.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, template, context)
