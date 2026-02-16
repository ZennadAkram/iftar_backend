from django import forms
from django.contrib import admin
from .models import IftarLocation
from django.contrib.gis.geos import Point

class IftarLocationForm(forms.ModelForm):
    latitude = forms.FloatField(required=True)
    longitude = forms.FloatField(required=True)

    class Meta:
        model = IftarLocation
        fields = ['name', 'city', 'address', 'is_active', 'latitude', 'longitude']

    def save(self, commit=True):
        instance = super().save(commit=False)
        lat = self.cleaned_data['latitude']
        lon = self.cleaned_data['longitude']
        instance.location = Point(lon, lat)
        if commit:
            instance.save()
        return instance

@admin.register(IftarLocation)
class IftarLocationAdmin(admin.ModelAdmin):
    form = IftarLocationForm
    list_display = ('name', 'city', 'address', 'is_active', 'created_at')
