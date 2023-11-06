from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class MenuItem(MPTTModel):
    name = models.CharField(max_length=100)
    url = models.SlugField(max_length=100, blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = self.name
        super(MenuItem, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("menu:item_detail", kwargs={"url": self.url})

