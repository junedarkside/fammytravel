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
    """Stations - Bus stops, Train stations, Ports"""
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


# ============================================
# PRODUCT MODELS
# ============================================


class Product(models.Model):
    """Main Product table"""
    PRODUCT_TYPES = [
        ('transport.cablecar', 'Cable Car'),
        ('transport.train', 'Train'),
        ('transport.bus', 'Bus'),
        ('transport.ferry', 'Ferry'),
        ('transport.transfer', 'Transfer'),
        ('transport.flight', 'Flight'),
        ('accommodation.hotel', 'Hotel'),
        ('accommodation.apartment', 'Apartment'),
        ('accommodation.hostel', 'Hostel'),
        ('accommodation.resort', 'Resort'),
        ('activity.tour', 'Tour'),
        ('activity.attraction', 'Attraction'),
        ('activity.adventure', 'Adventure'),
        ('activity.cruise', 'Cruise'),
        ('pass.travel', 'Travel Pass'),
        ('pass.city', 'City Card'),
        ('pass.attraction', 'Attraction Pass'),
        ('dining.restaurant', 'Restaurant'),
        ('dining.experience', 'Food Experience'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('discontinued', 'Discontinued'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, related_name='products')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    product_type = models.CharField(max_length=50, choices=PRODUCT_TYPES)
    product_subtype = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    
    # Requirements
    min_age = models.IntegerField(blank=True, null=True)
    max_age = models.IntegerField(blank=True, null=True)
    min_height_cm = models.IntegerField(blank=True, null=True)
    max_height_cm = models.IntegerField(blank=True, null=True)
    max_weight_kg = models.IntegerField(blank=True, null=True)
    
    # Duration
    duration_min = models.IntegerField(blank=True, null=True)
    duration_max = models.IntegerField(blank=True, null=True)
    difficulty_level = models.CharField(max_length=20, blank=True, null=True)
    
    # Season
    season_start_month = models.IntegerField(blank=True, null=True)
    season_start_day = models.IntegerField(blank=True, null=True)
    season_end_month = models.IntegerField(blank=True, null=True)
    season_end_day = models.IntegerField(blank=True, null=True)
    season_notes = models.TextField(blank=True, null=True)
    
    # Booking
    booking_required = models.BooleanField(default=True)
    instant_confirmation = models.BooleanField(default=True)
    booking_deadline_hours = models.IntegerField(blank=True, null=True)
    meeting_point = models.TextField(blank=True, null=True)
    pickup_available = models.BooleanField(default=False)
    dropoff_available = models.BooleanField(default=False)
    
    # Additional
    languages = models.JSONField(default=list, blank=True)
    accessibility = models.TextField(blank=True, null=True)
    cancellation_policy = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ProductVariant(models.Model):
    """Product Variants - Adult, Child, Senior, etc."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    variant_name = models.CharField(max_length=100)
    variant_code = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    sort_order = models.IntegerField(default=0)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Product Variant'
        verbose_name_plural = 'Product Variants'

    def __str__(self):
        return f"{self.product.name} - {self.variant_name}"


class ProductPricing(models.Model):
    """Product Pricing"""
    PRICE_TYPES = [
        ('per_person', 'Per Person'),
        ('per_group', 'Per Group'),
        ('per_room', 'Per Room'),
        ('per_vehicle', 'Per Vehicle'),
        ('fixed', 'Fixed'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pricing')
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, blank=True, null=True, related_name='pricing')
    price_amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='CHF')
    price_type = models.CharField(max_length=20, choices=PRICE_TYPES, default='per_person')
    unit_quantity = models.IntegerField(default=1)
    valid_from = models.DateField(blank=True, null=True)
    valid_until = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Product Pricing'
        verbose_name_plural = 'Product Pricings'

    def __str__(self):
        return f"{self.product.name} - {self.price_amount} {self.currency}"


class ProductImage(models.Model):
    """Product Images"""
    IMAGE_TYPES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('360', '360 View'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    media_type = models.CharField(max_length=20, choices=IMAGE_TYPES, default='image')
    url = models.URLField(max_length=500)
    thumbnail_url = models.URLField(max_length=500, blank=True, null=True)
    caption = models.CharField(max_length=500, blank=True, null=True)
    alt_text = models.CharField(max_length=300, blank=True, null=True)
    sort_order = models.IntegerField(default=0)
    is_primary = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return f"{self.product.name} - {self.media_type}"


class ProductInclusion(models.Model):
    """Product Inclusions/Exclusions"""
    INCLUSION_TYPES = [
        ('included', 'Included'),
        ('excluded', 'Excluded'),
    ]
    CATEGORIES = [
        ('transport', 'Transport'),
        ('meal', 'Meal'),
        ('guide', 'Guide'),
        ('equipment', 'Equipment'),
        ('entry_fee', 'Entry Fee'),
        ('insurance', 'Insurance'),
        ('other', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inclusions')
    inclusion_type = models.CharField(max_length=20, choices=INCLUSION_TYPES, default='included')
    category = models.CharField(max_length=50, choices=CATEGORIES, blank=True, null=True)
    description = models.TextField()
    sort_order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Product Inclusion'
        verbose_name_plural = 'Product Inclusions'

    def __str__(self):
        return f"{self.product.name} - {self.description[:50]}"


class ProductTimetable(models.Model):
    """Product Timetable/Schedule"""
    DAYS_OF_WEEK = [
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday'),
    ]
    SEASONS = [
        ('summer', 'Summer'),
        ('winter', 'Winter'),
        ('all_year', 'All Year'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='timetables')
    day_of_week = models.IntegerField(choices=DAYS_OF_WEEK, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    frequency_min = models.IntegerField(blank=True, null=True)
    season = models.CharField(max_length=50, choices=SEASONS, blank=True, null=True)
    notes = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'Product Timetable'
        verbose_name_plural = 'Product Timetables'

    def __str__(self):
        return f"{self.product.name} - {self.start_time}"


class ProductDiscount(models.Model):
    """Product Discount Rules"""
    DISCOUNT_TYPES = [
        ('child', 'Child Discount'),
        ('group', 'Group Discount'),
        ('senior', 'Senior Discount'),
        ('student', 'Student Discount'),
        ('pass_holder', 'Pass Holder Discount'),
        ('early_bird', 'Early Bird'),
        ('last_minute', 'Last Minute'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='discounts')
    discount_name = models.CharField(max_length=200)
    discount_type = models.CharField(max_length=50, choices=DISCOUNT_TYPES)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    conditions = models.JSONField(blank=True, null=True)
    min_people = models.IntegerField(blank=True, null=True)
    max_people = models.IntegerField(blank=True, null=True)
    valid_from = models.DateField(blank=True, null=True)
    valid_until = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Product Discount'
        verbose_name_plural = 'Product Discounts'

    def __str__(self):
        return f"{self.product.name} - {self.discount_name}"


# ============================================
# BOOKING MODELS
# ============================================


class Booking(models.Model):
    """Main Booking table"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
        ('refunded', 'Refunded'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    booking_reference = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='bookings')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Contact
    contact_name = models.CharField(max_length=200)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    
    # Total
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='CHF')
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # Notes
    special_requests = models.TextField(blank=True, null=True)
    internal_notes = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        ordering = ['-created_at']

    def __str__(self):
        return self.booking_reference


class BookingItem(models.Model):
    """Booking Line Items"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='booking_items')
    variant = models.ForeignKey(ProductVariant, on_delete=models.SET_NULL, blank=True, null=True)
    
    # Booking details
    booking_date = models.DateField()
    booking_time = models.TimeField(blank=True, null=True)
    quantity = models.IntegerField(default=1)
    
    # Pricing
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Passenger details (for transfers, etc.)
    passenger_name = models.CharField(max_length=200, blank=True, null=True)
    passenger_email = models.EmailField(blank=True, null=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Booking Item'
        verbose_name_plural = 'Booking Items'

    def __str__(self):
        return f"{self.booking.booking_reference} - {self.product.name}"


class Payment(models.Model):
    """Payment Records"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
        ('cancelled', 'Cancelled'),
    ]
    METHODS = [
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('paypal', 'PayPal'),
        ('omise', 'Omise'),
        ('cash', 'Cash'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='CHF')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_method = models.CharField(max_length=20, choices=METHODS)
    
    # Payment gateway
    gateway_transaction_id = models.CharField(max_length=100, blank=True, null=True)
    gateway_response = models.JSONField(blank=True, null=True)
    
    # Timestamps
    paid_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return f"{self.booking.booking_reference} - {self.amount} {self.currency}"
