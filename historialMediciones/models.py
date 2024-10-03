import random
import datetime

def generar_fechas_aleatorias(mes, año, num_fechas):
    # Generar todas las fechas posibles en el mes
    fechas_posibles = [datetime.date(año, mes, dia) for dia in range(1, 29)]
    # Seleccionar un subconjunto de fechas de forma aleatoria
    fechas_seleccionadas = random.sample(fechas_posibles, num_fechas)
    # Ordenar las fechas seleccionadas
    fechas_seleccionadas.sort()
    return fechas_seleccionadas

def generar_coordenadas_aleatorias(num_coordenadas=10):
    lat_min, lat_max = -31.0, -29.5
    lon_min, lon_max = -72.5, -70.5
    
    coordenadas = []
    for _ in range(num_coordenadas):
        latitud = round(random.uniform(lat_min, lat_max), 6)
        longitud = round(random.uniform(lon_min, lon_max), 6)
        coordenadas.append((latitud, longitud))
    
    return coordenadas

def generar_mediciones_con_fechas(mes, año):
    mediciones = []
    fechas = generar_fechas_aleatorias(mes, año, 10)
    coordenadas = generar_coordenadas_aleatorias(10)
    limite_permitido = 0.5
    for fecha, (latitud, longitud) in zip(fechas, coordenadas):
        valor = round(random.uniform(0.1, 1.0), 2)
        ubicacion_fuente = f"Latitud: {latitud}, Longitud: {longitud}"
        cumple_limite = valor <= limite_permitido
        mediciones.append({'valor': valor, 'fecha': fecha, 'ubicacion_fuente': ubicacion_fuente, 'cumple_limite': cumple_limite})
    return mediciones





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
                "mediciones": generar_mediciones_con_fechas(1, 2024),
            },
            "febrero": {
                "mediciones": generar_mediciones_con_fechas(2, 2024),
            },
            "marzo": {
                "mediciones": generar_mediciones_con_fechas(3, 2024),
            },
            "abril": {
                "mediciones": generar_mediciones_con_fechas(4, 2024),
            },
            "mayo": {
                "mediciones": generar_mediciones_con_fechas(5, 2024),
            },
            "junio": {
                "mediciones": generar_mediciones_con_fechas(6, 2024),
            },
            "julio": {
                "mediciones": generar_mediciones_con_fechas(7, 2024),
            },
            "agosto": {
                "mediciones": generar_mediciones_con_fechas(8, 2024),
            },
            "septiembre": {
                "mediciones": generar_mediciones_con_fechas(9, 2024),
            },
            "octubre": {
                "mediciones": generar_mediciones_con_fechas(10, 2024),
            },
            "noviembre": {
                "mediciones": generar_mediciones_con_fechas(11, 2024),
            },
            "diciembre": {
                "mediciones": generar_mediciones_con_fechas(12, 2024),
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
                "mediciones": generar_mediciones_con_fechas(1, 2024),
            },
            "febrero": {
                "mediciones": generar_mediciones_con_fechas(2, 2024),
            },
            "marzo": {
                "mediciones": generar_mediciones_con_fechas(3, 2024),
            },
            "abril": {
                "mediciones": generar_mediciones_con_fechas(4, 2024),
            },
            "mayo": {
                "mediciones": generar_mediciones_con_fechas(5, 2024),
            },
            "junio": {
                "mediciones": generar_mediciones_con_fechas(6, 2024),
            },
            "julio": {
                "mediciones": generar_mediciones_con_fechas(7, 2024),
            },
            "agosto": {
                "mediciones": generar_mediciones_con_fechas(8, 2024),
            },
            "septiembre": {
                "mediciones": generar_mediciones_con_fechas(9, 2024),
            },
            "octubre": {
                "mediciones": generar_mediciones_con_fechas(10, 2024),
            },
            "noviembre": {
                "mediciones": generar_mediciones_con_fechas(11, 2024),
            },
            "diciembre": {
                "mediciones": generar_mediciones_con_fechas(12, 2024),
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
                "mediciones": generar_mediciones_con_fechas(1, 2024),
            },
            "febrero": {
                "mediciones": generar_mediciones_con_fechas(2, 2024),
            },
            "marzo": {
                "mediciones": generar_mediciones_con_fechas(3, 2024),
            },
            "abril": {
                "mediciones": generar_mediciones_con_fechas(4, 2024),
            },
            "mayo": {
                "mediciones": generar_mediciones_con_fechas(5, 2024),
            },
            "junio": {
                "mediciones": generar_mediciones_con_fechas(6, 2024),
            },
            "julio": {
                "mediciones": generar_mediciones_con_fechas(7, 2024),
            },
            "agosto": {
                "mediciones": generar_mediciones_con_fechas(8, 2024),
            },
            "septiembre": {
                "mediciones": generar_mediciones_con_fechas(9, 2024),
            },
            "octubre": {
                "mediciones": generar_mediciones_con_fechas(10, 2024),
            },
            "noviembre": {
                "mediciones": generar_mediciones_con_fechas(11, 2024),
            },
            "diciembre": {
                "mediciones": generar_mediciones_con_fechas(12, 2024),
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
                "mediciones": generar_mediciones_con_fechas(1, 2024),
            },
            "febrero": {
                "mediciones": generar_mediciones_con_fechas(2, 2024),
            },
            "marzo": {
                "mediciones": generar_mediciones_con_fechas(3, 2024),
            },
            "abril": {
                "mediciones": generar_mediciones_con_fechas(4, 2024),
            },
            "mayo": {
                "mediciones": generar_mediciones_con_fechas(5, 2024),
            },
            "junio": {
                "mediciones": generar_mediciones_con_fechas(6, 2024),
            },
            "julio": {
                "mediciones": generar_mediciones_con_fechas(7, 2024),
            },
            "agosto": {
                "mediciones": generar_mediciones_con_fechas(8, 2024),
            },
            "septiembre": {
                "mediciones": generar_mediciones_con_fechas(9, 2024),
            },
            "octubre": {
                "mediciones": generar_mediciones_con_fechas(10, 2024),
            },
            "noviembre": {
                "mediciones": generar_mediciones_con_fechas(11, 2024),
            },
            "diciembre": {
                "mediciones": generar_mediciones_con_fechas(12, 2024),
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
                "mediciones": generar_mediciones_con_fechas(1, 2024),
            },
            "febrero": {
                "mediciones": generar_mediciones_con_fechas(2, 2024),
            },
            "marzo": {
                "mediciones": generar_mediciones_con_fechas(3, 2024),
            },
            "abril": {
                "mediciones": generar_mediciones_con_fechas(4, 2024),
            },
            "mayo": {
                "mediciones": generar_mediciones_con_fechas(5, 2024),
            },
            "junio": {
                "mediciones": generar_mediciones_con_fechas(6, 2024),
            },
            "julio": {
                "mediciones": generar_mediciones_con_fechas(7, 2024),
            },
            "agosto": {
                "mediciones": generar_mediciones_con_fechas(8, 2024),
            },
            "septiembre": {
                "mediciones": generar_mediciones_con_fechas(9, 2024),
            },
            "octubre": {
                "mediciones": generar_mediciones_con_fechas(10, 2024),
            },
            "noviembre": {
                "mediciones": generar_mediciones_con_fechas(11, 2024),
            },
            "diciembre": {
                "mediciones": generar_mediciones_con_fechas(12, 2024),
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
                "mediciones": generar_mediciones_con_fechas(1, 2024),
            },
            "febrero": {
                "mediciones": generar_mediciones_con_fechas(2, 2024),
            },
            "marzo": {
                "mediciones": generar_mediciones_con_fechas(3, 2024),
            },
            "abril": {
                "mediciones": generar_mediciones_con_fechas(4, 2024),
            },
            "mayo": {
                "mediciones": generar_mediciones_con_fechas(5, 2024),
            },
            "junio": {
                "mediciones": generar_mediciones_con_fechas(6, 2024),
            },
            "julio": {
                "mediciones": generar_mediciones_con_fechas(7, 2024),
            },
            "agosto": {
                "mediciones": generar_mediciones_con_fechas(8, 2024),
            },
            "septiembre": {
                "mediciones": generar_mediciones_con_fechas(9, 2024),
            },
            "octubre": {
                "mediciones": generar_mediciones_con_fechas(10, 2024),
            },
            "noviembre": {
                "mediciones": generar_mediciones_con_fechas(11, 2024),
            },
            "diciembre": {
                "mediciones": generar_mediciones_con_fechas(12, 2024),
            }
        }
    }
}

# Actualizar las mediciones para incluir la última fecha y valor de medición
for area in areas_protegidas.values():
    for mes, datos in area["mediciones_mensuales_2024"].items():
        if datos["mediciones"]:
            ultima_medicion = datos["mediciones"][-1]
            datos["ultima_fecha_medicion"] = ultima_medicion["fecha"]
            datos["ultimo_valor_medicion"] = ultima_medicion["valor"]