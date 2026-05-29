from django.contrib import admin
from .models import UnsafeZone

@admin.register(UnsafeZone)
class UnsafeZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'radius', 'added_at')
    list_filter = ('added_at',)
    search_fields = ('name',)
