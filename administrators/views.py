# from administrators.models import Employee
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
    fnEmpData = Employee.objects.values_list('first_name')
    context = {
        'empData': empData,
        'form': form,
        'fnEmpData': fnEmpData
    }
    return render(request, 'administrators/HomePage.html', context)


# def viewEmployees(request):
#     empData = Employee.objects.all()
#     return render(request, 'administrators/HomePage.html', {'empData': empData})


# def modifyEmployees(request):
#     data1 = Employee.objects.values_list('first_name')
#     return render(request, 'administrators/HomePage.html', {'data1': data1})
