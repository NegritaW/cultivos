from django.shortcuts import render

def listar_cultivos(request):
    cultivos_originales = [
        {'nombre': 'Tomate', 'tipo': 'fruto'},
        {'nombre': 'Lechuga', 'tipo': 'hoja'},
        {'nombre': 'Albahaca', 'tipo': 'hoja'},
        {'nombre': 'Zanahoria', 'tipo': 'raiz'},
        {'nombre': 'Cilantro', 'tipo': 'hoja'},
        {'nombre': 'Pimiento', 'tipo': 'fruto'},
    ]
    termino = request.GET.get('buscar', '')
    tipo = request.GET.get('tipo', '')
    cultivo_filtrados = cultivos_originales
    if termino:
        cultivo_filtrados = [c for c in cultivo_filtrados if termino.lower() in c['nombre'].lower()]
    if tipo:
        cultivo_filtrados = [c for c in cultivo_filtrados if c['tipo'] == tipo]
    
    contexto = {
        'titulo': 'Mi huerto',
        'mensaje': 'Filtra los cultivos por nombre y tipo',
        'cultivos': cultivo_filtrados,
    }
    return render(request, 'cultivos/lista_cultivos.html', contexto)

def detalle_cultivo(request, nombre):
    cultivos = {
        'Tomate': {
            'tipo':'fruto',
            'descripcion':'Requiere sol directo y riego moderado, muy sensible al frio',
            'siembra':'Agosto-Octubre',
            'cosecha':'Noviembre-Enero'
        },
        'Lechuga': {
            'tipo':'hoja',
            'descripcion':'Requiere sombra y riego constante, suelo humedo',
            'siembra':'Marzo-Mayo',
            'cosecha':'60 dias despues de la siembra'
        },
        'Albahaca': {
            'tipo':'hoja',
            'descripcion':'Climas calidos, no tolerancia a heladas',
            'siembra':'Septiembre-Noviembre',
            'cosecha':'40 dias despues de la siembra'
        },
        'Zanahoria': {
            'tipo':'raiz',
            'descripcion':'Requiere sol directo y riego moderado, muy sensible al frio',
            'siembra':'Agosto-Octubre',
            'cosecha':'Noviembre-Enero'
        },
        'Cilantro': {
            'tipo':'hoja',
            'descripcion':'Requiere sol directo y riego moderado, muy sensible al frio',
            'siembra':'Agosto-Octubre',
            'cosecha':'Noviembre-Enero'
        },
        'Pimiento': {
            'tipo':'fruto',
            'descripcion':'Requiere sol directo y riego moderado, muy sensible al frio',
            'siembra':'Agosto-Octubre',
            'cosecha':'Noviembre-Enero'
        },
    }
    cultivos = cultivos.get(nombre)
    if not cultivos:
        return render(request, 'cultivos/no_encontrado.html', {'nombre':nombre})
    contexto ={
        'nombre':nombre,
        'tipo':cultivos['tipo'],
        'descripcion':cultivos['descripcion'],
        'siembra':cultivos['siembra'],
        'cosecha':cultivos['cosecha'],
    }
    return render(request, 'cultivos/detalle.html', contexto)

def recomendar_cultivo(request):
    cultivos_por_estacion = {
        'verano': {'nombre': 'Albahaca', 'tipo': 'hoja'},
        'otonio': {'nombre': 'Tomate', 'tipo': 'fruto'},
        'invierno': {'nombre': 'Cilantro', 'tipo': 'hoja'},
        'primavera': {'nombre': 'Pimiento', 'tipo': 'fruto'},
    }

    estacion_front = request.GET.get('estacion', '')

    if estacion_front and estacion_front in cultivos_por_estacion:
        cultivos_filtrados = [cultivos_por_estacion[estacion_front]]
    else:
        cultivos_filtrados = list(cultivos_por_estacion.values())

    print("DEBUG cultivos_filtrados:", cultivos_filtrados)

    contexto = {
        'cultivos': cultivos_filtrados,
    }
    return render(request, 'cultivos/lista_cultivos.html', contexto)

def consejo_diario(request, consejo):
    pass

def evaluar_riego(request, riego):
    pass

def calculador_espacio(request, espacio):
    pass