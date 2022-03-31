from django.contrib.auth import get_user_model
from django.db.models import Q
from users.forms import UserUpdateForm, UserRegisterForm
from users.models import Log
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from users.decorators import administrator_required
from django.apps import apps
from django.core.paginator import Paginator

User = get_user_model()

@login_required
@administrator_required
def base(request):
    return redirect('administrators:employees')


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
    paginator = Paginator(all_logs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'administrators/log.html', {'logs': page_obj})
  
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
            user_type='hospital_staff') | Q(user_type='administrator')).order_by('user_type', 'username')
    
    paginator = Paginator(employees, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'form': form,
        'employees': page_obj,
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

            messages.info(request, f'Employee: {username} has been deleted')
            return redirect('administrators:employees')

        if u_form.is_valid():
            u_form.save()

            messages.success(request, f'Your account has been updated!')
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
