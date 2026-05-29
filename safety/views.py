import json

from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import UnsafeZone

DEFAULT_ZONES = [
    {
        'name': 'Downtown Red Zone',
        'latitude': 12.9716,
        'longitude': 77.5946,
        'radius': 500,
    },
    {
        'name': 'Neighborhood Danger',
        'latitude': 12.9352,
        'longitude': 77.6245,
        'radius': 450,
    },
    {
        'name': 'Market Unsafe Zone',
        'latitude': 12.9923,
        'longitude': 77.6340,
        'radius': 420,
    },
]


def home(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def navigation(request):
    return render(request, 'navigation.html')

def safety_zones(request):
    return render(request, 'safety_zones.html')

def guardian(request):
    return render(request, 'guardian.html')

def reports(request):
    return render(request, 'reports.html')


def ensure_default_zones():
    if UnsafeZone.objects.exists():
        return

    for zone_data in DEFAULT_ZONES:
        UnsafeZone.objects.create(**zone_data)


@require_http_methods(['GET'])
def api_zones(request):
    ensure_default_zones()
    zones = list(
        UnsafeZone.objects.values('id', 'name', 'latitude', 'longitude', 'radius')
    )
    return JsonResponse({'zones': zones})


@csrf_exempt
@require_http_methods(['POST'])
def api_report(request):
    try:
        body = json.loads(request.body.decode('utf-8'))
        latitude = float(body.get('latitude'))
        longitude = float(body.get('longitude'))
        radius = int(body.get('radius', 450))
        name = body.get('name', 'Reported Unsafe Zone')
    except (ValueError, TypeError, json.JSONDecodeError):
        return HttpResponseBadRequest('Invalid JSON payload')

    if not (-90 <= latitude <= 90 and -180 <= longitude <= 180 and radius > 0):
        return HttpResponseBadRequest('Invalid location or radius values')

    zone = UnsafeZone.objects.create(
        name=name,
        latitude=latitude,
        longitude=longitude,
        radius=radius,
    )
    return JsonResponse(
        {
            'id': zone.id,
            'name': zone.name,
            'latitude': zone.latitude,
            'longitude': zone.longitude,
            'radius': zone.radius,
        }
    )