from django.shortcuts import render

# Create your views here.



def index(request):
	message = 'Hola Index'
	return render(request, 'index.html', {'msg': message})


def registro(request, methods=['GET', 'POST']):
	pass


