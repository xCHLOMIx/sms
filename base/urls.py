from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView, name = "home"),
    path('inventory/', inventoryView, name = "inventory"),
    path('inventory/add-product', addProductView, name = "add-product"),
    path('inventory/delete-product/<str:pk>', deleteView, name = "delete-product"),
    path('inventory/update-product/<str:pk>', updateView, name = "update-product"),
    path('users/logout/', logoutView, name = "logout")
]
