from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView, name = "home"),
    path('inventory/', inventoryView, name = "inventory"),
    path('inventory/add-product', addProductView, name = "add-product"),
    path('inventory/delete-product/<str:pk>', deleteView, name = "delete-product"),
    path('product-in/', productInView, name = "product-in"),
    path('product-out/', productOutView, name = "product-out"),
    path('stock-in-report/', stockInReportView, name = "stock-in-report"),
    path('stock-out-report/', stockOutReportView, name = "stock-out-report"),
    path('update-product/<str:pk>', updateView, name = "update-product"),
    path('users/logout/', logoutView, name = "logout")
]
