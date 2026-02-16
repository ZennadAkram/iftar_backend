from rest_framework import serializers
from .models import IftarLocation
from django.contrib.gis.geos import Point

class IftarLocationSerializer(serializers.ModelSerializer):
    latitude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()

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
        ]

    def get_latitude(self, obj):
        return obj.location.y

    def get_longitude(self, obj):
        return obj.location.x

    def create(self, validated_data):
        lat = validated_data.pop('latitude', None)
        lng = validated_data.pop('longitude', None)
        if lat is not None and lng is not None:
            validated_data['location'] = Point(lng, lat)
        return super().create(validated_data)
