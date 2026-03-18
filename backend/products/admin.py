from django.contrib import admin
from .models import (
    Country, Destination, Operator, OperatorDestination,
    Station, Route, RouteStation
)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'code_2', 'code_3', 'region']
    search_fields = ['name', 'code_2', 'code_3']
    list_filter = ['region']


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'destination_type', 'is_active']
    list_filter = ['country', 'destination_type', 'is_active']
    search_fields = ['name', 'country__name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ['name', 'operator_type', 'subtype', 'rating']
    list_filter = ['operator_type', 'subtype']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ['name', 'destination', 'station_type', 'is_active']
    list_filter = ['station_type', 'is_active']
    search_fields = ['name', 'destination__name']


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ['name', 'operator', 'route_type', 'distance_km', 'journey_time_min', 'is_active']
    list_filter = ['route_type', 'is_active']
    search_fields = ['name', 'operator__name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(RouteStation)
class RouteStationAdmin(admin.ModelAdmin):
    list_display = ['route', 'station', 'sequence', 'journey_time_from_prev_min']
    list_filter = ['route__operator']
    ordering = ['route', 'sequence']
