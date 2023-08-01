import pandas as pd
import plotly.express as px
from django.shortcuts import render

def interactive_chart(request):
    # Datos de ejemplo (reemplazar esto con tus propios datos)
    data = {
        'Ciudad': ['Nueva York', 'Los Ángeles', 'Chicago', 'Houston', 'Phoenix'],
        'Poblacion': [8175133, 3792621, 2695598, 2100263, 1445632]
    }

    # Convertir los datos en un DataFrame de pandas
    df = pd.DataFrame(data)

    # Crear la gráfica de barras interactiva con Plotly
    fig = px.bar(df, x='Ciudad', y='Poblacion', title='Población por Ciudad')

    # Convertir la gráfica en formato JSON para enviarla al template
    chart = fig.to_json()

    # Renderizar el template con la gráfica
    return render(request, 'chart.html', {'chart': chart})
