from django.urls import path
from .views import NearestIftarLocationsView

urlpatterns = [
    path('nearest/', NearestIftarLocationsView.as_view(), name='nearest-iftar'),
]
