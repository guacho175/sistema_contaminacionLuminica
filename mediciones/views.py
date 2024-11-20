from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import MedicionForm
from .models import Medicion
from proyectos.models import Proyecto
import folium
from folium.plugins import MarkerCluster








