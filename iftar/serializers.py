from rest_framework import serializers
from .models import IftarLocation
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

class IftarLocationSerializer(serializers.ModelSerializer):
    latitude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()
    distance = serializers.SerializerMethodField()  # distance in km

    class Meta:
        model = IftarLocation
        fields = [
            'id',
            'name',
            'city',
            'address',
            'is_active',
            'latitude',
            'longitude',
            'distance',  # include distance
        ]

    def get_latitude(self, obj):
        return obj.location.y

    def get_longitude(self, obj):
        return obj.location.x

    def get_distance(self, obj):
     if hasattr(obj, 'distance_m') and obj.distance_m is not None:
        return round(obj.distance_m.km, 2)
     return None



    def create(self, validated_data):
        lat = validated_data.pop('latitude', None)
        lng = validated_data.pop('longitude', None)
        if lat is not None and lng is not None:
            validated_data['location'] = Point(lng, lat)
        return super().create(validated_data)
