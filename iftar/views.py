from rest_framework.generics import ListAPIView
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import IftarLocation
from .serializers import IftarLocationSerializer

class NearestIftarLocationsView(ListAPIView):
    serializer_class = IftarLocationSerializer

    def get_queryset(self):
        # Get user's latitude and longitude from query params
        lat = self.request.query_params.get('lat')
        lng = self.request.query_params.get('lng')

        queryset = IftarLocation.objects.filter(is_active=True)

        try:
            lat = float(lat)
            lng = float(lng)
            user_location = Point(lng, lat, srid=4326)

            # Annotate distance and order by nearest
            queryset = queryset.annotate(distance=Distance('location', user_location)).order_by('distance')
        except (TypeError, ValueError):
            # If user location not provided or invalid, return all active
            pass

        return queryset
