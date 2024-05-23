from django.shortcuts import render, get_object_or_404
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


def get_json_data(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    context = {
        'title' : place.title
    }
    return render(request, 'place.html', context=context)