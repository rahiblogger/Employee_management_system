from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Employee, Role, Department
from .form import *
# Create your views here.


def index(request):
    return render(request, "index.html", {})


def all_emp(request):
    all_employee = Employee.objects.all()
    return render(request, "all_employee.html", {"all_employee": all_employee})


def add_emp(request):
    all_employee = Employee.objects.all()
    if request.method == "POST":
        print(request.POST)
        new_employee = Employee(
            first_name=request.POST.get("firstName"),
            last_name=request.POST.get("lastName"),
            dept_id=request.POST.get("department"),
            salary=request.POST.get("salary"),
            bonus=request.POST.get("bonus"),
            role_id=request.POST.get("role"),
            phone=request.POST.get("phone"),
            hire_date=request.POST.get("date"),
        )
        new_employee.save()
        return redirect("/all_emp")

    else:
        # form = AddEmployee()
        return render(request, "add_emp.html", {"roles": Role.objects.all(), "depts": Department.objects.all()})


def remove_emp(request, id=None):
    if id:
        try:
            emp = Employee.objects.get(id=id)
            emp.delete()
            return redirect("/all_emp")
        except:
            return HttpResponse("Invalid Response")
    all_emp = Employee.objects.all()
    return render(request, "remove_emp.html", {"all_emp": all_emp})


def filter_emp(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST["name"]
        department = request.POST["department"]
        role = request.POST["role"]
        emp = Employee.objects.all()
        if name:
            emp = emp.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if department:
            emp = emp.filter(dept__name__icontains=department)
        if role:
            emp = emp.filter(role__name__icontains=role)
        return render(request, "all_employee.html", {"all_employee": emp})
    else:
        return render(request, "filter_emp.html")
