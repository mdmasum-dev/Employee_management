from django.shortcuts import render,redirect
from empolyapp.models import *


# Create your views here.

def Employee_list(request):
    
    Employee_Data = EmployeeModel.objects.all()
    
    context = {
        'Employee_Data':Employee_Data
    }
    
    return render(request,'Employee_list.html',context)


def add_employee(request):
    if request.method == "POST":
        emp_Id=request.POST.get('emp_Id')
        emp_name=request.POST.get('emp_name')
        department=request.POST.get('department')
        emp_picture=request.FILES.get('emp_picture')
        
        EmployeeModel.objects.create(
            emp_Id=emp_Id,
            emp_name=emp_name,
            department=department,
            emp_picture=emp_picture,
        ).save()
        return redirect('Employee_list')
    
    return render(request,'add_employee.html')


def edit_employee(request,id):
    
    Employee_Data = EmployeeModel.objects.get(id=id)
    
    if request.method == "POST":
        Employee_Data.emp_Id=request.POST.get('emp_Id')
        Employee_Data.emp_name=request.POST.get('emp_name')
        Employee_Data.department=request.POST.get('department')
        
        if request.FILES.get('emp_picture'):
            Employee_Data.emp_picture=request.FILES.get('emp_picture')
        Employee_Data.save()
        
        return redirect('Employee_list')
    
    context = {
        'Employee_Data':Employee_Data
    }
    
    return render(request,'edit_employee.html',context)


def Delete_employee(request,id):
    
    EmployeeModel.objects.get(id=id).delete()
    
    return redirect('Employee_list')
    