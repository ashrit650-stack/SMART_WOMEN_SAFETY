from django.db import models

class UnsafeZone(models.Model):
    name = models.CharField(max_length=120, default='Unsafe Zone')
    latitude = models.FloatField()
    longitude = models.FloatField()
    radius = models.PositiveIntegerField(default=400)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.latitude:.5f}, {self.longitude:.5f})"
