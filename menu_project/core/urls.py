from django.contrib import admin
from django.urls import path
from menu.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/", IndexView.as_view()),
]
