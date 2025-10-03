from django.shortcuts import render, redirect
from .forms import CultivoForm
from .models import Cultivo

def registrar_cultivo(request):
    if request.method == 'POST':
        form = CultivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cultivos') #Nombre URL del listado
    else:
        form = CultivoForm()
    return render(request, 'cultivos/registrar_cultivo.html', {'form':form})
        
def listar_cultivos(request):
    cultivos = Cultivo.objects.all()
    return render(request, 'cultivos/lista_cultivos.html',{
        'titulo': 'Listado de Cultivos',
        'cultivos':cultivos
    })

def detalle_cultivo(request, nombre):
    pass