import pandas as pd
import plotly.express as px
from django.http import HttpResponse
from django.shortcuts import render
import json

def index(request):
    #return HttpResponse("Hello, world!")
    return render(request, "plotlyapp/index.html")

def interactive_chart(request):
    # Datos de ejemplo (reemplazar esto con tus propios datos)
    #data = {
    #    'Poblacion': [8175133, 3792621, 2695598, 2100263, 1445632]
    #    'Ciudad': ['Nueva York', 'Los Ángeles', 'Chicago', 'Houston', 'Phoenix'],
    #}
    data = {
        "Poblacion": [8175133, 3792621, 2695598, 2100263, 1445632],
        "Ciudad": ["Nueva York", "Los Ángeles", "Chicago", "Houston", "Phoenix"]
    }
    df = pd.DataFrame(data)

    # Crear la gráfica de barras interactiva con Plotly
    fig = px.bar(df, x='Ciudad', y='Poblacion', title='Población por Ciudad')

    data2 = [{"x": [1, 2, 3, 4, 5], "y": [10, 11, 12, 13, 14], "type": 'scatter', "mode": 'lines+markers', "name": 'Línea 1'}]
    layout = {
            "title": "Gráfica Interactiva",
            "xaxis": {
                "title": "Eje X"
            },
            "yaxis": {
                "title": "Eje Y"
            }
        }

    # Convertir los datos en un DataFrame de pandas
    #df = pd.DataFrame(data)

    # Crear la gráfica de barras interactiva con Plotly
    #fig = px.bar(df, x='Ciudad', y='Poblacion', title='Población por Ciudad')

    # Convertir la gráfica en formato JSON para enviarla al template
    chart = fig.to_json()

    # Renderizar el template con la gráfica
    return render(request, 'plotly/chart.html', {"data": chart, "data2":json.dumps(data2), "layout":json.dumps(layout)})
