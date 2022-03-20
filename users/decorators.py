from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy


def patient_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the logged-in user is a patient,
    redirects to the log-in page if necessary.
    """
    login_url = reverse_lazy('login-user', kwargs={'usertype': 'patient'})
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.user_type == 'patient',
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def hospital_staff_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the logged-in user is a hospital-staff,
    redirects to the log-in page if necessary.
    """
    login_url = reverse_lazy('login-user', kwargs={'usertype': 'staff'})
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.user_type == 'hospital_staff',
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def doctor_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the logged-in user is a doctor,
    redirects to the log-in page if necessary.
    """
    login_url = reverse_lazy('login-user', kwargs={'usertype': 'staff'})
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.user_type == 'doctor',
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def insurance_staff_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the logged-in user is an insurance-staff,
    redirects to the log-in page if necessary.
    """
    login_url = reverse_lazy('login-user', kwargs={'usertype': 'staff'})
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.user_type == 'insurance_staff',
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def lab_staff_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the logged-in user is a lab-staff,
    redirects to the log-in page if necessary.
    """
    login_url = reverse_lazy('login-user', kwargs={'usertype': 'staff'})
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.user_type == 'lab_staff',
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def administrator_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the logged-in user is an administrator,
    redirects to the log-in page if necessary.
    """
    login_url = reverse_lazy('login-user', kwargs={'usertype': 'staff'})
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.user_type == 'administrator',
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
