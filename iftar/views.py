from rest_framework.generics import ListAPIView
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import IftarLocation
from .serializers import IftarLocationSerializer

class NearestIftarLocationsView(ListAPIView):
    serializer_class = IftarLocationSerializer

    def get_queryset(self):
        queryset = IftarLocation.objects.filter(is_active=True)
        lat = self.request.query_params.get('lat')
        lng = self.request.query_params.get('lng')

        if lat is not None and lng is not None:
            try:
                lat = float(lat)
                lng = float(lng)
                user_location = Point(lng, lat, srid=4326)

                # Annotate queryset with distance in meters
                queryset = queryset.annotate(
                    distance_m=Distance('location', user_location)
                ).order_by('distance_m')

                # Save user_location for serializer
                self.user_location = user_location
            except ValueError:
                self.user_location = None
        else:
            self.user_location = None

        return queryset

    def get_serializer_context(self):
        # Pass user_location to serializer
        context = super().get_serializer_context()
        context['reference_point'] = getattr(self, 'user_location', None)
        return context
