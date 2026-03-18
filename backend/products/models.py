from django.db import models
from django.utils.text import slugify
import uuid


class Country(models.Model):
    """Countries table"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    code_2 = models.CharField(max_length=2, blank=True, null=True)
    code_3 = models.CharField(max_length=3, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    currency_symbol = models.CharField(max_length=5, blank=True, null=True)
    timezone = models.CharField(max_length=50, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class Destination(models.Model):
    """Destinations - Cities, Regions, Islands"""
    DESTINATION_TYPES = [
        ('city', 'City'),
        ('mountain', 'Mountain'),
        ('beach', 'Beach'),
        ('island', 'Island'),
        ('region', 'Region'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='destinations')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    destination_type = models.CharField(max_length=50, choices=DESTINATION_TYPES, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Destination'
        verbose_name_plural = 'Destinations'

    def __str__(self):
        return f"{self.name}, {self.country.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Operator(models.Model):
    """Tour Operators"""
    OPERATOR_TYPES = [
        ('transport', 'Transport'),
        ('activity', 'Activity'),
        ('accommodation', 'Accommodation'),
        ('dining', 'Dining'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    operator_type = models.CharField(max_length=50, choices=OPERATOR_TYPES)
    subtype = models.CharField(max_length=50, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    logo_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    established_year = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Operator'
        verbose_name_plural = 'Operators'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class OperatorDestination(models.Model):
    """Operators in destinations"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, related_name='operator_destinations')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='operator_destinations')
    is_primary = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Operator Destination'
        verbose_name_plural = 'Operator Destinations'

    def __str__(self):
        return f"{self.operator.name} - {self.destination.name}"


class Station(models.Model):
    """Stations - Bus stops, Train stations, Ports, etc."""
    STATION_TYPES = [
        ('airport', 'Airport'),
        ('port', 'Port'),
        ('train_station', 'Train Station'),
        ('bus_station', 'Bus Station'),
        ('valley_station', 'Valley Station'),
        ('middle_station', 'Middle Station'),
        ('summit_station', 'Summit Station'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='stations')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    station_type = models.CharField(max_length=50, choices=STATION_TYPES, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    altitude_m = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    timezone = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Station'
        verbose_name_plural = 'Stations'

    def __str__(self):
        return f"{self.name} ({self.station_type})"


class Route(models.Model):
    """Routes"""
    ROUTE_TYPES = [
        ('one_way', 'One Way'),
        ('round_trip', 'Round Trip'),
        ('circuit', 'Circuit'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, related_name='routes')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    route_type = models.CharField(max_length=50, choices=ROUTE_TYPES, blank=True, null=True)
    distance_km = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    journey_time_min = models.IntegerField(blank=True, null=True)
    max_gradient = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'

    def __str__(self):
        return self.name


class RouteStation(models.Model):
    """Route Stations - sequence of stations"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='route_stations')
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='route_stations')
    sequence = models.IntegerField()
    journey_time_from_prev_min = models.IntegerField(blank=True, null=True)
    distance_from_prev_km = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = 'Route Station'
        verbose_name_plural = 'Route Stations'
        ordering = ['sequence']
        unique_together = ['route', 'sequence']

    def __str__(self):
        return f"{self.route.name} - {self.sequence}. {self.station.name}"
