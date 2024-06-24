# ReunionMap/map/views.py
import json
import requests
from django.shortcuts import render
from .models import Randonnee
from django.core.serializers import serialize
from django.http import JsonResponse

# Create your views here.
def map_view(request):
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

    return render(request, 'map/map.html', { 'data': combined_data_json})
