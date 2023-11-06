from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from menu.models import MenuItem


class MenuItemAdmin(MPTTModelAdmin):
    list_display = ('name', 'url', 'parent', 'is_active')


admin.site.register(MenuItem, MenuItemAdmin)
