from django.urls import path
from . import views # the dot(.) denotes base

urlpatterns = [
    path('',views.home),
    path('products/',views.products),
    path('customer/',views.customer)
]
