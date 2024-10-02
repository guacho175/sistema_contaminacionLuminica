import random
import datetime


def generar_mediciones():
    return [round(random.uniform(0.1, 1.0), 2) for _ in range(10)]


def generar_fecha_aleatoria(mes, año):
    dia = random.randint(1, 28)  # máximo de 28 días para todos los meses
    return datetime.date(año, mes, dia)


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
        "imagen": "Bosque-Fray-Jorge.jpg",
        "mediciones_mensuales_2024": {
            "enero": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(1, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "febrero": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(2, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "marzo": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(3, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "abril": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(4, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "mayo": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(5, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "junio": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(6, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "julio": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(7, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "agosto": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(8, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "septiembre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(9, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "octubre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(10, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "noviembre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(11, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "diciembre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(12, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            }
        }
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
        "imagen": "La-Campana.jpg",
        "mediciones_mensuales_2024": {
            "enero": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(1, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "febrero": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(2, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "marzo": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(3, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "abril": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(4, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "mayo": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(5, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "junio": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(6, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "julio": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(7, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "agosto": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(8, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "septiembre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(9, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "octubre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(10, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "noviembre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(11, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "diciembre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(12, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            }
        }
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
        "imagen": "Rio-Clarillo.jpg",
        "mediciones_mensuales_2024": {
            "enero": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(1, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "febrero": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(2, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "marzo": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(3, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "abril": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(4, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "mayo": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(5, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "junio": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(6, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "julio": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(7, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "agosto": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(8, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "septiembre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(9, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "octubre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(10, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "noviembre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(11, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "diciembre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(12, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            }
        }
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
        "imagen": "Pinguino-Humboldt.jpg",
        "mediciones_mensuales_2024": {
            "enero": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(1, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "febrero": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(2, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "marzo": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(3, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "abril": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(4, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "mayo": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(5, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "junio": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(6, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "julio": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(7, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "agosto": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(8, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "septiembre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(9, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "octubre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(10, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "noviembre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(11, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "diciembre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(12, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            }
        }
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
        "imagen": "Las-Chinchillas.jpg",
        "mediciones_mensuales_2024": {
            "enero": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(1, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "febrero": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(2, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "marzo": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(3, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "abril": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(4, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "mayo": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(5, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "junio": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(6, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "julio": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(7, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "agosto": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(8, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "septiembre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(9, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "octubre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(10, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "noviembre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(11, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "diciembre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(12, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            }
        }
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
        "imagen": "Pichasca.jpg",
        "mediciones_mensuales_2024": {
            "enero": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(1, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "febrero": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(2, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "marzo": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(3, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "abril": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(4, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "mayo": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(5, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "junio": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(6, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "julio": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(7, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
              "agosto": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(8, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "septiembre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(9, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "octubre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(10, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "noviembre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(11, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            },
            "diciembre": {
                "mediciones": generar_mediciones(),
                "ultima_fecha_medicion": generar_fecha_aleatoria(12, 2024),
                "ultimo_valor_medicion": generar_mediciones()[-1]
            }
        }
    }
}