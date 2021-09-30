from django.shortcuts import render

# Create your views here.



def index(request):
    message = 'Hola'
    return render(request, 'encuestaSituacional/index.html', {'message': message})