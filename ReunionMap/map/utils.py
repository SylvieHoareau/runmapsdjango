# map/utils.py

import requests

def get_arcgis_token(username, password):
    token_url = 'https://www.arcgis.com/sharing/rest/generateToken'
    params = {
        'f': 'json',
        'username': username,
        'password': password,
        'referer': 'http://www.arcgis.com',
        'expiration': 60
    }
    response = requests.post(token_url, data=params)
    data = response.json()
    if 'token' in data:
        return data['token']
    else:
        raise Exception('Erreur lors de l\'obtention du token: {}'.format(data))