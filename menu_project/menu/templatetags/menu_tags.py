from django import template
from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('index.html')
def draw_menu():
    item_list = MenuItem.objects.all()
    return {"item_list": item_list}
