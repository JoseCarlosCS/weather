import requests
from django.core.management.base import BaseCommand
import datetime
import math

def convert_datetime(a):
    # using strptime() to get datetime object
    datetime_obj = datetime.datetime.strptime(a, '%Y-%m-%dT%H:%M:%S%z')
    print(datetime_obj)
    return datetime_obj


def get_info():
    url = 'https://globalmet.mx/estaciones/conditions/78/'
    url_two = 'https://globalmet.mx/api/v2/pronosticos/348/'
    r = requests.get(url, headers={'Authorization':      
        'Token ea86a649b495c8cb159b32a89099359503f8ff28'})
    now = r.json()
    future_data = requests.get(url_two, headers={'Authorization':      
        'Token ea86a649b495c8cb159b32a89099359503f8ff28'})
    future_data = future_data.json()
    return [now, future_data]



def clean_data():
    # Diccionario de informacion actual
    current = dict()

    # Diccionario de pronosticos
    future_list = []

    # Obtiene la informacion de la API
    info = get_info()

    # Ordenar info
    fecha_medicion = info[0]['current_observation']['fecha_medicion']
    current['fecha_medicion']=convert_datetime(fecha_medicion)
    temp_c = info[0]['current_observation']['temp_c']
    temp_c = math.trunc(temp_c)
    print(temp_c)
    current['temp_c']=info[0]['current_observation']['temp_c']
    temp_f = (temp_c * 1.8) + 32 
    temp_f = math.trunc(temp_f)
    print(temp_f)
    current['temp_f']=temp_f
    current['wind_kph']=info[0]['current_observation']['wind_kph']
    current['wind_mph']=round(0.6214 * current['wind_kph'], 2)
    current['wind_dir_degrees']=info[0]['current_observation']['wind_dir_degrees']
    current['relative_humidity']=info[0]['current_observation']['relative_humidity']
    current['eto']=info[0]['current_observation']['eto']


    
    for i in info[1]:
        new_dict = dict()
        new_dict['fecha'] = i['fecha']
        new_dict['temp_max_c'] = i['temp_max_c']
        new_dict['temp_min_c'] = i['temp_min_c']
        new_dict['temp_prom_c'] = i['temp_prom_c']
        new_dict['hum_max_porc'] = i['hum_max_porc']
        new_dict['hum_prom_porc'] = i['hum_prom_porc']
        new_dict['hum_min_porc'] = i['hum_min_porc']
        new_dict['viento_max_kmh'] = i['viento_max_kmh']
        new_dict['viento_max_mph'] = i['viento_max_mph']
        future_list.append(new_dict)

    print(current)
    print(future_list)
    return [current, future_list]


