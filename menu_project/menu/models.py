from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class MenuItem(MPTTModel):
    name = models.CharField(max_length=100)
    name_url = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

