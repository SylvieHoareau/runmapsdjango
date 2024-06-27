from django.db import models

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
    

class Forest(models.Model):
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
    
class Natura(models.Model):
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