from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin),
    path('customer/', views.customer),
]
