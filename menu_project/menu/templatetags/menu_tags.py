from django import template
from menu.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu = MenuItem.objects.filter(name=menu_name).first()
    if menu:
        return render_menu(menu)


def render_menu(menu_item):
    """menu rendering"""
    output = f'<ul>'
    for item in menu_item.get_children():
        output += f'<li><a href="{item.url}">{item.name}</a>'
        if item.is_active:
            output += render_menu(item)
        output += '</li>'
    output += '</ul>'
    return output