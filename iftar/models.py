from django.contrib.gis.db import models

class IftarLocation(models.Model):
    name = models.CharField(max_length=200)
    
    city = models.CharField(max_length=100)
    location = models.PointField(geography=True)

    address = models.CharField(max_length=255)

   
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.city}"
