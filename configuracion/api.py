import requests
import time
from datetime import datetime, timedelta

# Configuración de la API de Fitbit
USER_ID = 'C9WXR7'
ACCESS_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1BWWUoiLCJzdWIiOiJDOVdYUjciLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJlY2cgcnNldCByaXJuIHJveHkgcnBybyBybnV0IHJzbGUgcmNmIHJhY3QgcmxvYyBycmVzIHJ3ZWkgcmhyIHJ0ZW0iLCJleHAiOjE3MzAwMTAxOTcsImlhdCI6MTcyOTk4MTM5N30.6DVQu6cHBB8B-T1h_NWGQyxkGbpKcsiHXfgyv0IjVI0'
REFRESH_TOKEN = '2d3fe1b9ec7ed47b390dd8b8eb84bf2f07499127cf39266185089801cf6de507'
BASE_URL = 'https://api.fitbit.com/1/user'
EXPIRES_IN = 3600  # Duración del token en segundos
TOKEN_OBTAINED = time.time()  # Marca de tiempo de obtención del token

# Verifica si el token ha expirado
def is_token_expired():
    return time.time() - TOKEN_OBTAINED > EXPIRES_IN

# Función para refrescar el token de acceso
def refresh_access_token():
    global ACCESS_TOKEN, TOKEN_OBTAINED
    url = 'https://api.fitbit.com/oauth2/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic 23PVYJ:YjQxZGUyYzliZTQ3YTRlMGUyZDE1OTc0ZjE2NGMyOGI=' # Asegúrate de codificar en Base64
    }
    data = {'grant_type': 'refresh_token', 'refresh_token': REFRESH_TOKEN}
    
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        token_data = response.json()
        ACCESS_TOKEN = token_data['access_token']
        REFRESH_TOKEN = token_data['refresh_token']
        TOKEN_OBTAINED = time.time()
        return ACCESS_TOKEN
    else:
        raise Exception("Error al refrescar el token de acceso")

# Funciones para obtener datos de Fitbit
def get_steps(period='today'):
    if is_token_expired():
        refresh_access_token()
    url = f'{BASE_URL}/{USER_ID}/activities/steps/date/{period}/1d.json'
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return int(data['activities-steps'][0]['value']) if data['activities-steps'] else 0
    else:
        return 0  

def get_calories(period='today'):
    if is_token_expired():
        refresh_access_token()
    url = f'{BASE_URL}/{USER_ID}/activities/calories/date/{period}/1d.json'
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return int(data['activities-calories'][0]['value']) if data['activities-calories'] else 0
    else:
        return 0  

def get_distance(period='today'):
    if is_token_expired():
        refresh_access_token()
    url = f'{BASE_URL}/{USER_ID}/activities/distance/date/{period}/1d.json'
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return float(data['activities-distance'][0]['value']) if data['activities-distance'] else 0
    else:
        return 0  
def get_steps_week():
    if is_token_expired():
        refresh_access_token()
    today = datetime.now()
    week_start = today - timedelta(days=today.weekday())  # Lunes de esta semana
    url = f'{BASE_URL}/{USER_ID}/activities/steps/date/{week_start.strftime("%Y-%m-%d")}/7d.json'
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}', 'Content-Type': 'application/json'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return [int(day['value']) for day in data['activities-steps']] if data['activities-steps'] else [0] * 7
    else:
        return [0] * 7

def get_calories_week():
    if is_token_expired():
        refresh_access_token()
    today = datetime.now()
    week_start = today - timedelta(days=today.weekday())  # Lunes de esta semana
    url = f'{BASE_URL}/{USER_ID}/activities/calories/date/{week_start.strftime("%Y-%m-%d")}/7d.json'
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}', 'Content-Type': 'application/json'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return [int(day['value']) for day in data['activities-calories']] if data['activities-calories'] else [0] * 7
    else:
        return [0] * 7

def get_steps_month():
    if is_token_expired():
        refresh_access_token()
    today = datetime.now()
    month_start = today.replace(day=1)  # Primer día del mes
    url = f'{BASE_URL}/{USER_ID}/activities/steps/date/{month_start.strftime("%Y-%m-%d")}/30d.json'
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}', 'Content-Type': 'application/json'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return [int(day['value']) for day in data['activities-steps']] if data['activities-steps'] else [0] * 30
    else:
        return [0] * 30

def get_calories_month():
    if is_token_expired():
        refresh_access_token()
    today = datetime.now()
    month_start = today.replace(day=1)  # Primer día del mes
    url = f'{BASE_URL}/{USER_ID}/activities/calories/date/{month_start.strftime("%Y-%m-%d")}/30d.json'
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}', 'Content-Type': 'application/json'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return [int(day['value']) for day in data['activities-calories']] if data['activities-calories'] else [0] * 30
    else:
        return [0] * 30

def get_distance_week():
    if is_token_expired():
        refresh_access_token()
    today = datetime.now()
    week_start = today - timedelta(days=today.weekday())  # Lunes de esta semana
    url = f'{BASE_URL}/{USER_ID}/activities/distance/date/{week_start.strftime("%Y-%m-%d")}/7d.json'
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}', 'Content-Type': 'application/json'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return [float(day['value']) for day in data['activities-distance']] if data['activities-distance'] else [0.0] * 7
    else:
        return [0.0] * 7

def get_distance_month():
    if is_token_expired():
        refresh_access_token()
    today = datetime.now()
    month_start = today.replace(day=1)  # Primer día del mes
    url = f'{BASE_URL}/{USER_ID}/activities/distance/date/{month_start.strftime("%Y-%m-%d")}/30d.json'
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}', 'Content-Type': 'application/json'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return [float(day['value']) for day in data['activities-distance']] if data['activities-distance'] else [0.0] * 30
    else:
        return [0.0] * 30
    
# Función principal para obtener datos de un periodo específico
def get_data(period='today'):
    return {
        'steps': get_steps(period),
        'calories': get_calories(period),
        'distance': get_distance(period)
    }
