from django.db import models

# Create your models here.
areas_protegidas = {
    101: {
        "nombre": "Parque Nacional Bosque Fray Jorge",
        "ubicacion": "Región de Coquimbo",
        "latitud": -30.6683,
        "longitud": -71.6495,
        "tamaño_area_km2": 100,
        "especies_sensibles": ["Puma", "Huemul", "Águila Chilena"],
        "altitud_promedio_m": 600,
        "fuentes_cercanas_de_contaminacion": "Pueblos cercanos, carreteras",
        "nivel_brillo_cielo_nocturno": "Escala Bortle 2-3",
        "valor_ultima_medicion": 0.15,
        "fecha_ultima_medicion": "25-09-2024",
        "imagen": "Bosque-Fray-Jorge.jpg"
    },
    102: {
        "nombre": "Parque Nacional La Campana",
        "ubicacion": "Región de Valparaíso",
        "latitud": -32.9533,
        "longitud": -71.1141,
        "tamaño_area_km2": 80,
        "especies_sensibles": ["Zorro Culpeo", "Chincol", "Huemul"],
        "altitud_promedio_m": 1200,
        "fuentes_cercanas_de_contaminacion": "Pueblos y rutas cercanas",
        "nivel_brillo_cielo_nocturno": "Escala Bortle 3-4",
        "valor_ultima_medicion": 0.35,
        "fecha_ultima_medicion": "28-09-2024",
        "imagen": "Bosque-Fray-Jorge.jpg"
    },
    103: {
        "nombre": "Parque Nacional Río Clarillo",
        "ubicacion": "Región Metropolitana",
        "latitud": -33.8267,
        "longitud": -70.4489,
        "tamaño_area_km2": 85,
        "especies_sensibles": ["Cóndor", "Zorro Culpeo", "Lagarto Nítido"],
        "altitud_promedio_m": 750,
        "fuentes_cercanas_de_contaminacion": "Carreteras y áreas urbanas cercanas",
        "nivel_brillo_cielo_nocturno": "Escala Bortle 4-5",
        "valor_ultima_medicion": 0.22,
        "fecha_ultima_medicion": "30-09-2024",
        "imagen": "Bosque-Fray-Jorge.jpg"
    },
    104: {
        "nombre": "Parque Nacional Pingüino de Humboldt",
        "ubicacion": "Región de Atacama y Coquimbo",
        "latitud": -29.2572,
        "longitud": -71.4083,
        "tamaño_area_km2": 88,
        "especies_sensibles": ["Pingüino de Humboldt", "Delfín nariz de botella", "León Marino"],
        "altitud_promedio_m": 50,
        "fuentes_cercanas_de_contaminacion": "Faros y pequeñas poblaciones costeras",
        "nivel_brillo_cielo_nocturno": "Escala Bortle 2",
        "valor_ultima_medicion": 0.12,
        "fecha_ultima_medicion": "29-09-2024",
        "imagen": "Bosque-Fray-Jorge.jpg"
    },
    105: {
        "nombre": "Reserva Nacional Las Chinchillas",
        "ubicacion": "Región de Coquimbo",
        "latitud": -31.6462,
        "longitud": -71.2203,
        "tamaño_area_km2": 45,
        "especies_sensibles": ["Chinchilla", "Guanaco", "Águila Mora"],
        "altitud_promedio_m": 500,
        "fuentes_cercanas_de_contaminacion": "Pueblos cercanos",
        "nivel_brillo_cielo_nocturno": "Escala Bortle 2-3",
        "valor_ultima_medicion": 0.19,
        "fecha_ultima_medicion": "27-09-2024",
        "imagen": "Bosque-Fray-Jorge.jpg"
    },
    106: {
        "nombre": "Monumento Natural Pichasca",
        "ubicacion": "Región de Coquimbo",
        "latitud": -30.2654,
        "longitud": -70.8958,
        "tamaño_area_km2": 1.28,
        "especies_sensibles": ["Zorro Chilla", "Cóndor Andino", "Loro Tricahue"],
        "altitud_promedio_m": 400,
        "fuentes_cercanas_de_contaminacion": "Pueblos y pequeñas rutas",
        "nivel_brillo_cielo_nocturno": "Escala Bortle 3",
        "valor_ultima_medicion": 0.28,
        "fecha_ultima_medicion": "26-09-2024",
        "imagen": "Bosque-Fray-Jorge.jpg"
    }
}



