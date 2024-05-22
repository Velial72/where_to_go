from django.shortcuts import render
from places.models import Place

def show_index(request):
    places = Place.objects.all()
    for place in places:
        features = [
            {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
                },
            "properties": {
                "title": place.title,
                "placeId": place.place_id,
                "detailsUrl": f"static/places/{place.place_id}.json"
                }
            }
            ]


    context = {
        'places_geojson': {
            "type": "FeatureCollection",
            "features": features
        }
    }

    return render(request, "index.html", context = context)
