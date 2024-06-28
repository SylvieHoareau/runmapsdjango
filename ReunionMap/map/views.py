# ReunionMap/map/views.py
import json
import requests
from django.shortcuts import render
from .models import Randonnee, ForetPublique
from django.core.serializers import serialize
from django.http import JsonResponse
from django.contrib.gis.geos import Polygon, MultiPolygon
import xml.etree.ElementTree as ET

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
    url = "https://data.geopf.fr/wfs/ows?SERVICE=WFS&TYPENAMES=BDTOPO_V3:foret_publique&REQUEST=GetFeature&VERSION=2.0.0"
    headers = {
        'Content-Type': 'application/xml'
    }

    # Ajout d'un filtre pour récupérer uniquement les données pour La Réunion (code INSEE)
    xml_filter = """
        <wfs:GetFeature service="WFS" version="2.0.0"
            xmlns:wfs="http://www.opengis.net/wfs/2.0"
            xmlns:ogc="http://www.opengis.net/ogc"
            xmlns:gml="http://www.opengis.net/gml/3.2">
            <wfs:Query typeNames="BDTOPO_V3:foret_publique">
                <ogc: Filter>
                    <ogc: PropertyIsEqualTo>
                        <ogc: PropertyName>code_insee</PropertyName>
                        <ogc: Literal>974</Literal>
                    </ogc:PropertyIsEqualTo>
                </ogc:Filter>
            </wfs:Query>
        </wfs:GetFeature>
    """
    
    # Récupérer les données de l'API
    try:
        response = requests.get(url, data=xml_filter, headers=headers)
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
    forests = ForetPublique.objects.all()
    forests_data = list(forests.values())

    # Ajouter les données de l'API aux données du modèle Randonnee
    combined_data = forests_data + api_data

    # Convertir les données combinées en JSON
    combined_data_json = json.dumps(combined_data)

    return render(request, 'map/forest.html',  { 'data': combined_data_json})

# def parse_xml_and_save_to_db(xml_file_path):
#     if not xml_file_path:
#         return []
    
#     tree = ET.parse(xml_file_path)
#     root = tree.getRoot()

#     namespaces = {
#         'wfs': 'http://www.opengis.net/wf/2.0', 
#         'gml': 'http://www.opengis/gml/3.2',
#         'BDTOPO_V3': 'https://data.geopf.fr/wfs/ows?SERVICE=WFS&TYPENAMES=BDTOPO_V3:foret_publique&REQUEST=GetFeature&VERSION=2.0.0'
#     }

#     for member in root.findall('wfs:member', namespaces):
#         foret = member.find('BDTOPO_V3:foret_publique', namespaces)

#         cleabs = foret.find('BDTOPO_V3:cleabs', namespaces).text
#         nature = foret.find('BDTOPO_V3:nature', namespaces).text
#         toponyme = foret.find('BDTOPO_V3:toponyme', namespaces).text
#         statut_du_toponyme = foret.find('BDTOPO_V3:statut_du_toponyme', namespaces).text
#         importance = int(foret.find('BDTOPO_V3:importance', namespaces).text)
#         date_creation = foret.find('BDTOPO_V3:date_creation', namespaces).text
#         date_modification = foret.find('BDTOPO_V3:date_modification', namespaces).text
#         date_de_confirmation = foret.find('BDTOPO_V3:date_de_confirmation', namespaces).text
#         sources = foret.find('BDTOPO_V3:sources', namespaces).text
#         identifiants_sources = foret.find('BDTOPO_V3:identifiants_sources', namespaces).text
#         methode_d_acquisition_planimetrique = foret.find('BDTOPO_V3:methode_d_acquisition_planimetrique', namespaces).text
#         precision_planimetrique = float(foret.find('BDTOPO_V3:precision_planimetrique', namespaces).text)

#         # Geometrie
#         multi_surface = foret.find('.//gml:MultiSurface', namespaces)
#         surfaces = []

#         for surface_member in multi_surface.findall('gml:surfaceMember', namespaces):
#             polygon = surface_member.find('gml:Polygon', namespaces)
#             exterior = polygon.find('.//gml:exterior/gml:LinearRing/gml:posList', namespaces)
#             pos_list = exterior.text.strip().split()
#             coords = [(float(pos_list[i], float(pos_list[i + 1])) for i in range(0, len(pos_list), 2))]
#             surfaces.append(Polygon(coords))

#         geometrie = MultiPolygon(surfaces)

#         # Créer et enregistrer l'objet ForetPublique
#         foret_publique = ForetPublique(
#             cleabs = cleabs,
#             nature=nature,
#             toponyme=toponyme,
#             statut_du_toponyme=statut_du_toponyme,
#             importance=importance,
#             date_creation=date_creation,
#             date_modification=date_modification,
#             date_de_confirmation=date_de_confirmation,
#             sources=sources,
#             identifiants_sources=identifiants_sources,
#             methode_d_acquisition_planimetrique=methode_d_acquisition_planimetrique,
#             precision_planimetrique=precision_planimetrique

#         )

#         foret_publique.save()
