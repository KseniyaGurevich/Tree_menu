from django.urls import path

from menu import views

app_name = 'menu'

urlpatterns = [
    path("", views.index, name='index'),
    path('<slug:url>/', views.item_detail, name='item_detail'),
]