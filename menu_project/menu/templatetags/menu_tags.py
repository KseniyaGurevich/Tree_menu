from django import template
from menu.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(name, parent=None, parents=None):
    if parents is None:
        parents = []

    menu = MenuItem.objects.get(name=name)

    if menu.parent is not None:
        parents.append(menu.parent.name)

    if menu.parent is not None:
        draw_menu(name=menu.parent.name, parent=menu.name, parents=parents)

    return parents
