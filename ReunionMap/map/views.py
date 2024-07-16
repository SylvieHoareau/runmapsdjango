# ReunionMap/map/views.py
import json
import requests
from django.shortcuts import render
from .models import Randonnee, ForetPublique, Commune
from django.core.serializers import serialize
from django.http import JsonResponse
from django.contrib.gis.geos import Polygon, MultiPolygon
from django.conf import settings
from .utils import get_argis_token

# Create your views here.

def index_view(request):
    # Logique pour afficher la page d'accueil
    return render(request, 'map/index.html')

def rando_view(request):
    # points = PointOfInterest.objects.all()
    # points_json = serialize('json', points)
    # return render(request, 'map/map.html', {'points': points_json})

    # URL de l'API
    api_url = "https://data.regionreunion.com/api/explore/v2.1/catalog/datasets/circuits-rendonnees-lareunion-wssoubik/records?limit=100"

    # Récupérer les données de l'API
    try:
        response = requests.get(api_url)
        response.raise_for_status() # Vérifie si la requête a réussi
        api_data = response.json().get('results', [])
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des données de l'API : {e}")
        api_data = []
    # response = requests.get(api_url)
    # data = response.json()['results']

    # Debug : Afficher les données dans la console
    # print(data)

    # Vérifier les données dans la vie jSON
    #return JsonResponse(data, safe=False)

    # return render(request, 'map/map.html', {'data': data})

    # Récupérer les randonnées depuis le modèle Randonnée
    randonnees = Randonnee.objects.all()
    randonnees_data = list(randonnees.values())

    # Ajouter les données de l'API aux données du modèle Randonnee
    combined_data = randonnees_data + api_data

    # Convertir les données combinées en JSON
    combined_data_json = json.dumps(combined_data)

    return render(request, 'map/rando.html', { 'data': combined_data_json})

def forest_view(request):
    # Logique spécifique pour la page "forest"
    # Récupérer IGN_CLEF depuis les paramètres
    ign_clef = settings.IGN_CLEF

# Cleabs spécifiques
    cleabs = [
        "FORETPUB0000002204078552",
        "FORETPUB0000002204078551",
        "FORETPUB0000002204078549",
        "FORETPUB0000002204078547",
        "FORETPUB0000002204078546",
        "FORETPUB0000002204078545",
        "FORETPUB0000002204078544",
        "FORETPUB0000002204078543",
        "FORETPUB0000002204078540",
        "FORETPUB0000002204078538",
        "FORETPUB0000002204078537",
        "FORETPUB0000002204078536",
        "FORETPUB0000002204078535",
        "FORETPUB0000002204078529",
        "FORETPUB0000002204078528",
        "FORETPUB0000002204078527",
        "FORETPUB0000002204078526",
        "FORETPUB0000002204078525",
        "FORETPUB0000002204078524",
        "FORETPUB0000002204078523",
        "FORETPUB0000002204078522",
        "FORETPUB0000002204078521",
        "FORETPUB0000002204078520",
        "FORETPUB0000002204078519",
        "FORETPUB0000002204078518",
        "FORETPUB0000002204078517",
        "FORETPUB0000002204078516",
        "FORETPUB0000002204078515",
        "FORETPUB0000002204078514",
        "FORETPUB0000002204078513",
        "FORETPUB0000002204078512",
        "FORETPUB0000002204078511",
        "FORETPUB0000002204078510",
        "FORETPUB0000002204078509",
        "FORETPUB0000002204078508",
        "FORETPUB0000002204078506",
        "FORETPUB0000002204078504",
        "FORETPUB0000002204078503",
        "FORETPUB0000002204078501",
        "FORETPUB0000002204078500",
        "FORETPUB0000002204078499",
        "FORETPUB0000002204078498",
        "FORETPUB0000002204078469",
        "FORETPUB0000002204078468",
        "FORETPUB0000002204078459",
        "FORETPUB0000002204078458",
        "FORETPUB0000002204078457",
        "FORETPUB0000002204078456",
        "FORETPUB0000002204078454",
        "FORETPUB0000002204078453",
        "FORETPUB0000002204078452",
        "FORETPUB0000002204078451",
        "FORETPUB0000002204078450",
        "FORETPUB0000002204078449",
        "FORETPUB0000002204078448",
        "FORETPUB0000002204078447",
        "FORETPUB0000002204078446",
        "FORETPUB0000002204078445",
        "FORETPUB0000002204078444",
        "FORETPUB0000002204078443",
        "FORETPUB0000002204078442",
        "FORETPUB0000002204078441",
        "FORETPUB0000002204078440",
        "FORETPUB0000002204078439",
        "FORETPUB0000002204078438"
    ]
    
    communes = [
        97401,
        97402,
        97403,
        97404,
        97405,
        97406,
        97407,
        97408,
        97409,
        97410,
        97411,
        97412,
        97413,
        97414,
        97415,
        97416,
        97417,
        97418,
        97419,
        97420,
        97421,
        97422,
        97423,
        97424
    ]

    # Contruire le filtre CQL
    cql_filter_forest = ','.join([f"'{id}'" for id in cleabs])
    cql_filter_commune = ','.join([str(id) for id in communes])

    # URL de l'API IGN WFS
    forest_url = f"https://wxs.ign.fr/{ign_clef}/geoportail/wfs?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetFeature&TYPENAME=BDTOPO_V3:foret_publique&outputFormat=application/json&srsName=EPSG:4326&CQL_FILTER=cleabs%20IN%20({cql_filter_forest})"
    commune_url = f"https://wxs.ign.fr/{ign_clef}/geoportail/wfs?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetFeature&TYPENAME=ADMINEXPRESS-COG.LATEST:commune&outputFormat=application/json&srsName=EPSG:4326&CQL_FILTER=insee_com%20IN%20({cql_filter_commune})";

  
    # Logs pour le débogage
    # print("URL for forest data:", forest_url)
    # print("URL for commune data:", commune_url)

      # En-tête nécessaires pour la requête GET
    headers = {
        'Content-Type': 'application/json'
    }

    
    # Récupérer les données de l'API pour les forêts
    try:
        # Utilisez requests.post pour envoyer le filtre XML
        response_forest = requests.get(forest_url, headers=headers)
        response_forest.raise_for_status() # Vérifie si la requête a réussi

        # Affichage du contenu de la réponse pour le débogage
        #print("Contenu de la réponse de l'API :", response.text)   

        forest_data = response_forest.json().get('features', [])
    except (json.JSONDecodeError, requests.exceptions.RequestException) as e:
        print(f"Erreur lors de la récupération des données de l'API (forêt) : {e}")
        forest_data = []

  

     # Récupérer les données de l'API pour les communes
    try:
        # Utilisez requests.post pour envoyer le filtre XML
        response_commune = requests.get(commune_url, headers=headers)
        response_commune.raise_for_status() # Vérifie si la requête a réussi

        # Affichage du contenu de la réponse pour le débogage
        #print("Contenu de la réponse de l'API :", response.text)   

        commune_data = response_commune.json().get('features', [])
    except (json.JSONDecodeError, requests.exceptions.RequestException) as e:
        print(f"Erreur lors de la récupération des données de l'API (commune) : {e}")
        commune_data = []

    # Récupérer les données des forêts depuis le modèle ForetPublique
    forests = ForetPublique.objects.all()
    forest_data_db = list(forests.values())

     # Récupérer les données des communes depuis le modèle Commune
    communes = Commune.objects.all()
    commune_data_db = list(communes.values())

    # Ajouter les données de l'API aux données du modèle ForetPublique
    combined_data = {
        "forests": forest_data_db + forest_data,
        "communes":  commune_data_db + commune_data
    }
    # Convertir les données combinées en JSON
    combined_data_json = json.dumps(combined_data)

    #print("combined_data_json : ", combined_data_json) # Debug: afficher les données dans la console

    return render(request, 'map/forest.html',  { 'data': combined_data_json, 'IGN_CLEF': ign_clef})

# Débogage avec un seul code INSEE pour isoler le problème
def test_single_commune():
    ign_clef = settings.IGN_CLEF
    single_commune = 97401
    cql_filter__single_commune = f"code_insee={single_commune}"
    commune_url = f"https://wxs.ign.fr/{ign_clef}/geoportail/wfs?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetFeature&TYPENAME=ADMINEXPRESS-COG.LATEST:commune&outputFormat=application/json&srsName=EPSG:4326&CQL_FILTER={cql_filter__single_commune}"

    # print("URL for single commune data:", commune_url)

    try:
        response_commune = requests.get(commune_url)
        response_commune.raise_for_status()
        commune_data = response_commune.json().get('features', [])
        # print("Commune data:", commune_data)
    except (json.JSONDecodeError, requests.exceptions.RequestException) as e:
        print(f"Erreur lors de la récupération des données de l'API (commune) : {e}")

# Appelez cette fonction pour tester avec un seul code INSEE
test_single_commune()

def acrmap_view(request):
    username = 'username'
    password = 'password'

    try:
        token = get_argis_token(username, password)
    except Exception as e:
        return render(request, 'maps/arcmap.html', {'error': str(e)})

    # URL de l'API REST d'ArcGIS pour La Réunion
    url_arcgis = 'https://services.arcgis.com/arcgis/rest/services/ServiceName/FeatureServer/0/query'

    # Paramètres de la requête
    params = {
        'where': '1=1',
        'outfields': '*',
        'f': 'json',
        'token': token
    }

    response = requests.get(url_arcgis, params=params)
    data = response.json() if response.status_code == 200 else {}

    return render(request, 'maps/arcmap.html', {'data': data})
