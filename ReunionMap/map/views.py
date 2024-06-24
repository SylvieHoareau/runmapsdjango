from django.shortcuts import render
from .models import PointOfInterest
from django.core.serializers import serialize

# Create your views here.
def map_view(request):
    points = PointOfInterest.objects.all()
    points_json = serialize('json', points)
    return render(request, 'map/map.html', {'points': points_json})