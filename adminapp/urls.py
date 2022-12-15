from django.urls import path
from . import views

urlpatterns = [
    path('adminindex/',views.adminindex,name='adminindex')
]