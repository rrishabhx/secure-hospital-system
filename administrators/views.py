# from administrators.models import Employee
import re

from django.http import HttpResponseRedirect
from administrators.models import Employee
from .forms import CreateEmployeeForm
from django.contrib import messages
from django.shortcuts import render

def home(request):
    form = CreateEmployeeForm()

    if request.method == "POST":
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            # messages.success(request, f'Account created for {username}! You are now able to log in')
            # login(request, user)

            # return redirect('login')
            messages.success(request, f'Account created for {first_name}! You are now able to log in')
        else:
            messages.error(request, 'An error occurred during creation')

    empData = Employee.objects.all()
    fnEmpData = Employee.objects.values('first_name', 'last_name')
    context = {
        'empData': empData,
        'form': form,
        'fnEmpData': fnEmpData
    }
    return render(request, 'administrators/HomePage.html', context)


# def viewEmployees(request):
#     empData = Employee.objects.all()
#     return render(request, 'administrators/HomePage.html', {'empData': empData})


def deleteEmployees(request):
    
    # email_toDelete = request.GET['emailDelete']
    # first_name = Employee.objects.raw("select first_name from employee where email = "+str(email_toDelete)+";")
    variable = dict(request)
    return render(request, 'administrators/test.html', variable)
