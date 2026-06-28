from django.contrib import admin
from django.urls import path
from empolyapp.views import *

urlpatterns = [
    path('Employee_list/',Employee_list,name='Employee_list'),
    path('add_employee/',add_employee,name='add_employee'),
    path('edit_employee/<int:id>',edit_employee,name='edit_employee'),
    path('Delete_employee/<int:id>',Delete_employee,name='Delete_employee'),
]
