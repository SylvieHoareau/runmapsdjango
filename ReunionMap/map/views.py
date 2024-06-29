# ReunionMap/map/views.py
import json
import requests
from django.shortcuts import render
from .models import Randonnee, ForetPublique
from django.core.serializers import serialize
from django.http import JsonResponse
from django.contrib.gis.geos import Polygon, MultiPolygon
from django.conf import settings
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

    # Contruire le filtre CQL
    cql_filter = ','.join([f"'{id}'" for id in cleabs])

    # URL de l'API IGN WFS
    url = f"https://wxs.ign.fr/{ign_clef}/geoportail/wfs?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetFeature&TYPENAME=BDTOPO_V3:foret_publique&outputFormat=application/json&srsName=EPSG:4326&CQL_FILTER=cleabs%20IN%20({cql_filter})"


    # En-tête nécessaires pour la requête GET
    headers = {
        'Content-Type': 'application/json'
    }
    
    # Récupérer les données de l'API
    try:
        # Utilisez requests.post pour envoyer le filtre XML
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Vérifie si la requête a réussi
        # Affichage du contenu de la réponse pour le débogage
        #print("Contenu de la réponse de l'API :", response.text)   

        api_data = response.json().get('features', [])
       
    except json.JSONDecodeError:
        print(f"Erreur : la réponse de l'API n'est pas en format JSON : {e}")
        api_data = []
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des données de l'API : {e}")
        api_data = []

    # Récupérer les données des forêts depuis le modèle ForetPublique
    forests = ForetPublique.objects.all()
    forests_data = list(forests.values())

    # Ajouter les données de l'API aux données du modèle ForetPublique
    combined_data = forests_data + api_data
    # Convertir les données combinées en JSON
    combined_data_json = json.dumps(combined_data)

    #print("combined_data_json : ", combined_data_json) # Debug: afficher les données dans la console

    return render(request, 'map/forest.html',  { 'data': combined_data_json, 'IGN_CLEF': ign_clef})

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
