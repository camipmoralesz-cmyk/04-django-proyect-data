from django.shortcuts import render

def index(request):
    return render(request, 'inicio/default.html')
# #3 creamos una pequeña lista para que se nos vea en nuestro html
