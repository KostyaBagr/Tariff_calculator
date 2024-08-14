"""
URL configuration for main app.
"""
from django.urls import path
from .views import CalculatorView

urlpatterns = [

    path("tariff_calculator/calc/", CalculatorView.as_view(), name="tariff_calculator")
]