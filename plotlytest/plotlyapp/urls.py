from django.urls import path
from . import views

urlpatterns = [
    path('chart/', views.interactive_chart, name='interactive_chart'),
]
