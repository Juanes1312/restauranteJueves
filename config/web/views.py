from django.shortcuts import render

# Create your views here.
# las vistas(views)django son los controladores

# las vistas son las funciones de python 

def Home(request):
    return render(request, 'index.html')
