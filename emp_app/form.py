from django import forms
from .models import Department, Role

DEPT_CHOICES = [(department.id, department.name) for department in Department.objects.all()]
ROLE_CHOICES = [(role.name, role.name) for role in Role.objects.all()]


class AddEmployee(forms.Form):
    Firstname = forms.CharField(max_length=100, label="firstname")
    Lastname = forms.CharField(max_length=100)
    dept = forms.ChoiceField(choices=DEPT_CHOICES, label="Departments")
    Salary = forms.IntegerField()
    Role = forms.ChoiceField(choices=ROLE_CHOICES, label="Roles")
    Bonus = forms.IntegerField()
    phone = forms.IntegerField()
    hire_date = forms.DateField()