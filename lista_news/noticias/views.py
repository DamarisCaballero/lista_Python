from django.shortcuts import render, redirect
from django.http import HttpResponse


def filtrar_titulares(palabra_clave):
    # Lista de titulares de noticias
    titulares = [
        'Venta de armas en aumento',
        'Nuevas medidas de seguridad en aeropuertos',
        'Ciberataques afectan a grandes empresas',
        'Avances en la medicina contra el cáncer',
        'El cambio climático y sus consecuencias',
        'Inauguración de un nuevo centro educativo',
        # Agrega más titulares aquí
    ]

    # Filtrar los titulares que incluyen la palabra clave
    titulares_filtrados = [titular for titular in titulares if palabra_clave.lower() in titular.lower()]

    return titulares_filtrados


def home(request):
    if request.method == 'POST':
        # Obtener la palabra clave del formulario enviado
        palabra_clave = request.POST['palabra_clave']
        # Realizar la búsqueda y filtrar los titulares
        # (Debes completar esta parte según tu implementación)
        titulares_filtrados = filtrar_titulares(palabra_clave)
        # Pasar los titulares filtrados a la plantilla
        context = {
            'titulares': titulares_filtrados,
            'palabra_clave': palabra_clave,
        }
        return redirect('resultados')
    else:
        return render(request, 'noticias/home.html')

def resultados(request):
    palabra_clave = request.GET.get('palabra_clave')
    # Realizar la búsqueda y filtrar los titulares
    # (Debes completar esta parte según tu implementación)
    titulares_filtrados = filtrar_titulares(palabra_clave)
    # Pasar los titulares filtrados a la plantilla
    context = {
        'titulares': titulares_filtrados,
        'palabra_clave': palabra_clave,
    }
    return render(request, 'noticias/resultados.html', context)
