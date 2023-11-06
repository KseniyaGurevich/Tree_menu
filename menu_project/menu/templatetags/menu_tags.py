from django import template
from django.http import request
from django.shortcuts import get_object_or_404, render
from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag("menu.html")
def draw_menu(name):
    object = get_object_or_404(MenuItem, name=name)
    children = object.children.all()
    return {'object': object, 'children': 'children'}


@register.simple_tag
def draw_menu(menu_name):
    menu = MenuItem.objects.get(name=menu_name)
    children = menu.children.all()
    child_names = list(children.values_list("name", flat=True))
    result = {menu_name: child_names}
    return result


@register.inclusion_tag('menu.html')
def draw_menu2(menu_name):
    menu = MenuItem.objects.get(name=menu_name)
    children = menu.children.all()
    child_list = children.values_list("name", flat=True)
    print(child_list)
    return {'menu': menu}
