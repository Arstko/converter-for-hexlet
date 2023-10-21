import requests

URL = 'https://api.freecurrencyapi.com/v1/latest?apikey='
API_KEY = 'fca_live_MonqgBIWcuXXI7r6U4Iv8aXJ2z0OkCQ6DwrmAxI3'

def get_currencies():
    responce = requests.get(URL + API_KEY)
    return responce.json()