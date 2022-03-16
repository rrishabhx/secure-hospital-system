from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('hospital/', include('hospital.urls')),
    path('patients/', include('patients.urls')),
    path('doctors/', include('doctors.urls')),
    path('hospitalstaffs/', include('hospital_staffs.urls')),
    path('labstaffs/', include('lab_staffs.urls')),
    path('insurancestaffs/', include('insurance_staffs.urls')),
    path('admin_hospital/', include('administrators.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
