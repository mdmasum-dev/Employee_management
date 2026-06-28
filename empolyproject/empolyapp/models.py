from django.db import models


# Create your models here.

class EmployeeModel(models.Model):
    emp_Id = models.IntegerField(null=True)
    emp_name = models.CharField(max_length=100,null=True)
    department = models.CharField(max_length=100,null=True)
    emp_picture = models.ImageField(upload_to="Employee_picture",null=True)
    date = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.emp_name