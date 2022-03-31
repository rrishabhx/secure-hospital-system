# from administrators.models import Employee
from datetime import date

from django.contrib.auth import get_user_model
from django.db.models import Q

from administrators.models import Employee, Deleted_Employees
from users.forms import UserUpdateForm, UserRegisterForm
from users.models import Log
from .forms import CreateEmployeeForm
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from users.decorators import administrator_required
from django.apps import apps

User = get_user_model()


@login_required
@administrator_required
def create(request):
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
    return render(request, 'administrators/create.html', context)


# def viewEmployees(request):
#     empData = Employee.objects.all()
#     return render(request, 'administrators/HomePage.html', {'empData': empData})

@login_required
@administrator_required
def confirmDelete(request):
    email_toDelete = request.GET['emailDelete']
    first_name = request.GET['firstName']

    data1 = "select * from administrators_employee where first_name = '" + str(first_name) + "';"
    obj1 = Employee.objects.raw(data1)
    data = "select * from administrators_employee where email = '" + str(email_toDelete) + "';"
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

        Deleted_Employees.objects.create(first_name=str(fn), last_name=str(ln), employee_type=str(et),
                                         date_of_birth="1998-04-12", phone_number=str(pn), email=str(em),
                                         deleted_date=date.today())
        record = Employee.objects.get(email=str(email_toDelete))
        record.delete()
        messages.success(request, f'Record for {first_name} is deleted!')
        return redirect('administrators:create')
    else:
        messages.warning(request, f'Record for {first_name} is not deleted! Please check the email address given')
        return redirect('administrators:create')


@login_required
@administrator_required
def saveModify(request):
    firstName = request.GET['firstName']
    email_toModify = request.GET['emailModify']

    data1 = "select * from administrators_employee where first_name = '" + str(firstName) + "';"
    obj1 = Employee.objects.raw(data1)
    data = "select * from administrators_employee where email = '" + str(email_toModify) + "';"
    obj = Employee.objects.raw(data)

    for i in obj1:
        email_orig = i.email

    if str(email_orig) == email_toModify:
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
    else:
        messages.warning(request, f'Record for {firstName} is not updated! Please check the email address given')
        return redirect('administrators:modify')

    return render(request, 'administrators/modifyEmployee.html', context)


@login_required
@administrator_required
def save_modify(request):
    modify_fn = request.POST.get('first_name_modify')
    modify_ln = request.POST.get('last_name_modify')
    modify_emt = request.POST.get('employee_type_modify')
    modify_dob = request.POST.get('dob_modify')
    modify_ema = request.POST.get('email_modify')
    modify_phn = request.POST.get('phone_modify')

    record = Employee.objects.get(email=str(modify_ema))
    record.first_name = str(modify_fn)
    record.last_name = str(modify_ln)
    record.employee_type = str(modify_emt)
    record.date_of_birth = "1998-04-12"
    record.phone_number = str(modify_phn)
    record.save()

    messages.success(request, f'Record for {modify_fn} was updated!')
    return redirect('administrators:create')


@login_required
@administrator_required
def base(request):
    return redirect('administrators:profile')
    # return render(request, 'administrators/base.html')


@login_required
@administrator_required
def fetch(request):
    obj = Employee.objects.all()

    if obj.exists():
        context = {
            'empData': obj
        }
    else:
        context = {
            'empData': None
        }

    return render(request, 'administrators/viewEmployees.html', context)


@login_required
@administrator_required
def modify(request):
    obj = Employee.objects.all()
    fnEmpData = Employee.objects.values('first_name', 'last_name')

    if obj.exists():
        context = {
            'empData': obj,
            'fnEmpData': fnEmpData
        }
    else:
        context = {
            'empData': None,
            'fnEmpData': fnEmpData
        }
    return render(request, 'administrators/modify.html', context)


@login_required
@administrator_required
def delete(request):
    obj = Employee.objects.all()
    fnEmpData = Employee.objects.values('first_name', 'last_name')

    if obj.exists():
        context = {
            'empData': obj,
            'fnEmpData': fnEmpData
        }
    else:
        context = {
            'empData': None,
            'fnEmpData': fnEmpData
        }
    return render(request, 'administrators/delete.html', context)


@login_required
@administrator_required
def transactions(request):
    model = apps.get_model('hospital', 'Transaction')
    context = {'transactions': []}
    if request.method == 'POST':
        try:
            flag = request.POST['id']
            y = model.objects.get(id=flag)
            y.approved = True
            y.save()
            print(flag)
        except KeyError:
            print('KeyError')
    try:
        x = model.objects.filter(approved=None, completed=None)
        for i in x.iterator():
            context['transactions'].append(i)
    except:
        context['transactions'] = [['Record not found'] * 3]
    return render(request, 'administrators/transactions.html', context)


def log(request):
    all_logs = Log.objects.all().order_by('-date')
    return render(request, 'administrators/log.html', {'logs': all_logs})


@login_required
@administrator_required
def employees(request):
    print('Inside employees view')
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}!')

            return redirect('administrators:employees')
        else:
            messages.error(request, 'An error occurred during registration')

    employees = User.objects.filter(
        Q(user_type='doctor') | Q(user_type='insurance_staff') | Q(user_type='lab_staff') | Q(
            user_type='hospital_staff')).order_by('user_type', 'username')
    context = {
        'form': form,
        'employees': employees,
    }

    return render(request, 'administrators/employees.html', context=context)


@login_required
@administrator_required
def employees_detail(request, username):
    print('Inside employee detail view')
    user = User.objects.get(username=username)

    if request.method == 'POST':
        print("Request type: POST")
        u_form = UserUpdateForm(request.POST, instance=user)

        print(f'post data: {request.POST}')
        if 'delete_employee' in request.POST:
            print(f'Deleting employee {username}')
            user.delete()

            messages.info(request, f'Employee: {username} has been deleted!')
            return redirect('administrators:employees')

        if u_form.is_valid():
            u_form.save()

            messages.success(request, f'Employee: {username} has been updated!')
            return redirect('administrators:employees-detail', username=username)
    else:
        print(f"Request type: GET")
        u_form = UserUpdateForm(instance=user)

    context = {
        'u_form': u_form,
    }
    return render(request, 'administrators/employee_detail.html', context)


@login_required
@administrator_required
def profile(request):
    print("Inside Administrator profile")
    user = request.user

    if request.method == 'POST':
        print("Request type: POST")
        u_form = UserUpdateForm(request.POST, instance=user)

        if u_form.is_valid():
            u_form.save()

            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        print(f"Request type: GET")
        u_form = UserUpdateForm(instance=user)

    context = {
        'u_form': u_form,
    }

    return render(request, 'administrators/profile.html', context)
