
from django.urls import path

from apps.apuntes.views import Hola_Mundo

urlpatterns = [
    path('', Hola_Mundo)
]