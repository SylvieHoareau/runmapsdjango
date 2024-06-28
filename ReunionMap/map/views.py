# ReunionMap/map/views.py
import json
import requests
from django.shortcuts import render
from .models import Randonnee, ForetPublique
from django.core.serializers import serialize
from django.http import JsonResponse

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
 # URL de l'API
    api_url = "https://data.geopf.fr/wfs/ows?SERVICE=WFS&TYPENAMES=BDTOPO_V3:foret_publique&REQUEST=GetFeature&VERSION=2.0.0"

    # Ajout d'un filtre pour récupérer uniquement les données pour La Réunion (code INSEE)
    filter_param = """
        <Filter>
            <PropertyIsEqualTo>
                <PropertyName>code_insee</PropertyName>
                <Literal>974</Literal>
            </PropertyIsEqualTo>
        </Filter>
        """
    params = {
        'service': 'WFS',
        'version': '2.0.0',
        'request': 'GetFeature',
        'typenames': 'BDTOPO_V3:foret_publique',
        'filter': filter_param
    }
    
    # Récupérer les données de l'API
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status() # Vérifie si la requête a réussi
        api_data = response.json().get('features', [])
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
    forests = Forest.objects.all()
    forests_data = list(forests.values())

    # Ajouter les données de l'API aux données du modèle Randonnee
    combined_data = forests_data + api_data

    # Convertir les données combinées en JSON
    combined_data_json = json.dumps(combined_data)

    return render(request, 'map/forest.html',  { 'data': combined_data_json})

def parse_forest_data(xml_data):
    if not xml_data:
        return []
    
    tree = ET.ElementTree(ET.formstring(xml_data))
    root = tree.getRoot()

    namespace = {'wfs': 'http://www.opengis.net/wf/2.0', 'gml': 'http://www.opengis/gml/3.2'}

    features = root.findall('.//wfs:member', namespace)
    forests = []

    for feature in features:
        forest = {}
        properties = feature.find('.//BDTOPO_V3:foret_publique', namespace)
        if properties is not None:
            for prop in properties:
                tag = prop.tag.split('}')[-1]
                forest[tag] = prop.text
            forests.append(forest)
    
    return forests
