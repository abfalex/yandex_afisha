from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Location


def home(request):
    locations = Location.objects.all()
    features = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    float(location.lng),
                    float(location.lat),
                ],
            },
            "properties": {
                "title": location.title,
                "detailsUrl": reverse("location_detail", args=[location.pk]),
            },
        }
        for location in locations
    ]
    geojson_data = {"type": "FeatureCollection", "features": features}
    context = {"geojson_data": geojson_data}
    return render(request, "places/index.html", context=context)


def location_detail(request, id):
    place = get_object_or_404(Location.objects.prefetch_related("images"), id=id)
    images = place.images.all()
    data = {
        "title": place.title,
        "imgs": [image.image.url for image in images],
        "short_description": place.short_description,
        "long_description": place.long_description,
        "coordinates": {
            "lng": float(place.lng),
            "lat": float(place.lat),
        },
    }
    return JsonResponse(data, json_dumps_params={"ensure_ascii": False, "indent": 2})
