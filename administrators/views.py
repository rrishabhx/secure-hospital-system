# from administrators.models import Employee
from datetime import date
from administrators.models import Employee, Deleted_Employees
from .forms import CreateEmployeeForm
from django.contrib import messages
from django.shortcuts import redirect, render

def home(request):
    form = CreateEmployeeForm()

    if request.method == "POST":
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'Account created for {first_name}! You are now able to log in')
        else:
            messages.warning(request, 'An error occurred during creation')

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

    data1 = "select * from administrators_employee where first_name = '"+str(first_name)+"';"
    obj1 = Employee.objects.raw(data1)
    data = "select * from administrators_employee where email = '"+str(email_toDelete)+"';"
    obj = Employee.objects.raw(data)

    for i in obj1:
        email_orig = i.email

    if str(email_orig) == email_toDelete:
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
        messages.success(request, f'Record for {first_name} is deleted!')
        return redirect('administrators:home')
    else:
        messages.warning(request, f'Record for {first_name} is not deleted! Please check the email address given')
        return redirect('administrators:home')

def getEmployee(request):
    # firstName = request.GET['firstName']
    email_toModify = request.GET['emailModify']

    data = "select * from administrators_employee where email = '"+str(email_toModify)+"';"
    obj = Employee.objects.raw(data)

    for i in obj:
        fn = i.first_name
        ln = i.last_name
        db = i.date_of_birth
        et = i.employee_type
        pn = i.phone_number
        em = i.email

    context = {
        'fin': fn,
        'lan': ln,
        'dob': db,
        'emt': et,
        'phn': pn,
        'ema': em
    }

    return render(request, 'administrators/modifyEmployee.html', context)

def save_modify(request):
    modify_fn = request.POST.get('first_name_modify')
    modify_ln = request.POST.get('last_name_modify')
    modify_emt = request.POST.get('employee_type_modify')
    modify_dob = request.POST.get('dob_modify')
    modify_ema = request.POST.get('email_modify')
    modify_phn = request.POST.get('phone_modify')

    record = Employee.objects.get(email=str(modify_ema))
    record.first_name=str(modify_fn)
    record.last_name=str(modify_ln)
    record.employee_type=str(modify_emt)
    record.date_of_birth="1998-04-12"
    record.phone_number=str(modify_phn)
    record.save()

    messages.success(request, f'Record for {modify_fn} was updated!')
    return redirect('administrators:home')