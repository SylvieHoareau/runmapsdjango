from django.db import models
from django.contrib.gis.db import models as gis_models

# Create your models here.
class Randonnee(models.Model):
    nom = models.CharField(max_length=100)
    difficulte = models.CharField(max_length=1)
    distance_parcourue = models.FloatField()
    duree_minutes_total = models.IntegerField()
    altitude_min = models.IntegerField()
    altitude_max = models.IntegerField()
    location_lon = models.FloatField(null=True, blank=True)
    location_lat = models.FloatField(null=True, blank=True)
    is_ouvert = models.CharField(max_length=3)
    zone_translations_item_nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
    
class ForetPublique(models.Model):
    cleabs = models.CharField(max_length=255, unique=True)
    nature = models.CharField(max_length=255)
    toponyme = models.CharField(max_length=255)
    statut_du_toponyme = models.CharField(max_length=255)
    importance = models.IntegerField()
    date_creation = models.IntegerField()
    date_modification = models.DateTimeField()
    date_de_confirmation = models.DateTimeField()
    sources = models.CharField(max_length=255)
    identifiants_sources = models.CharField(max_length=255)
    methode_d_acquisition_planimetrique = models.CharField(max_length=255)
    precision_planimetrique = models.FloatField()
    geometrie = gis_models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.toponyme
    
class Commune(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    nom_m = models.CharField(max_length=100)
    insee_com = models.IntegerField( unique=True)
    statut = models.CharField(max_length=100)
    population = models.IntegerField()
    insee_can = models.IntegerField()
    insee_arr = models.IntegerField()
    insee_dep = models.IntegerField()
    insee_reg = models.IntegerField()
    insee_epci = models.IntegerField()
    geometrie = gis_models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.nom