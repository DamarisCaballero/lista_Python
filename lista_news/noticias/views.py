from django.shortcuts import render, redirect
from django.http import HttpResponse


def filtrar_titulares(palabra_clave):
    print("Palabra clave:", palabra_clave)  # Mensaje de impresión para verificar que se está ejecutando la función
    # Lista de titulares de noticias
    titulares = [
        "Aumenta la demanda de energías renovables",
        "Desarrollan vacuna efectiva contra el virus del dengue",
        "El mercado de criptomonedas experimenta volatilidad",
        "Descubren nueva especie de dinosaurio en América",
        "Avanza la investigación para la cura del Alzheimer",
        "Lanzamiento exitoso del satélite espacial comercial",
        "Nuevas regulaciones para proteger el medio ambiente",
        "Inauguración de un parque dedicado a la historia local",
        "Las ventas de carros eléctricos alcanzan cifras récord",
        "Investigadores descubren evidencias de vida en Marte",
        "Crece la preocupación por el calentamiento global",
        "Se detecta una nueva variante de virus informático",
        "Declaran emergencia sanitaria por brote de enfermedad",
        "Desarrollan tecnología para la generación de energía limpia",
        "Celebrities se unen para luchar contra el hambre en el mundo",
        "Avances en la inteligencia artificial transforman la industria",
        "Nuevo récord de producción de alimentos orgánicos",
        "Descubren posible cura para la diabetes tipo 2",
        "Conferencia aborda el futuro de la exploración espacial",
        "Invertir en bienes raíces: una opción segura",
    ]

    # Filtrar los titulares que incluyen la palabra clave
    titulares_filtrados = [titular for titular in titulares if palabra_clave.lower() in titular.lower()]

    return titulares_filtrados


def home(request):
    if request.method == 'POST':
        palabra_clave = request.POST.get('palabra_clave')
        print("Palabra clave ingresada:", palabra_clave)  # Mensaje de impresión para verificar que se obtiene la palabra clave
        if palabra_clave:
            return redirect('resultados')
        else:
            mensaje_error = 'Por favor, ingresa una palabra clave.'
            return render(request, 'noticias/home.html', {'mensaje_error': mensaje_error})
    return render(request, 'noticias/home.html')


