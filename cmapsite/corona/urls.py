from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path("", views.index, name="index"),
    path("chart/", views.chart, name="chart"),
]
