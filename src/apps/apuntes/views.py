from django.shortcuts import render

# Create your views here.


def Hola_Mundo(request):
    return render(request, 'holamundo.html', {})