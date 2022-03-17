# from administrators.models import Employee
from datetime import date
from django.http import HttpResponseRedirect
from administrators.models import Employee, Deleted_Employees
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
    form = CreateEmployeeForm()
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

    email_toDelete = request.GET['emailDelete']
    first_name = request.GET['firstName']

    data = "select * from administrators_employee where email = '"+str(email_toDelete)+"';"
    obj = Employee.objects.raw(data)
    
    for i in obj:
        fn = i.first_name
        ln = i.last_name
        db = i.date_of_birth
        et = i.employee_type
        pn = i.phone_number
        em = i.email
    

    Deleted_Employees.objects.create(first_name=str(fn), last_name=str(ln), employee_type=str(et), date_of_birth="1998-04-12", phone_number=str(pn), email=str(em), deleted_date=date.today())
    record = Employee.objects.get(email=str(email_toDelete))
    record.delete()

    context = {
        'em' : email_toDelete,
        'fn' : first_name,
        'out' : obj
    }
    return render(request, 'administrators/test.html', context )

def getEmployee(request):
    # firstName = request.GET['firstName']
    email_toModify = request.POST.get('emailModify', False)

    data = "select * from administrators_employee where email = '"+str(email_toModify)+"';"
    obj = Employee.objects.raw(data)

    return HttpResponseRedirect(request.path_info, {'out1':obj})