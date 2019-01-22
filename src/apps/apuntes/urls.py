
from django.urls import path

urlpatterns = [
    path('apunte/', include('apps.apuntes.urls'))
]