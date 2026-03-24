from django.contrib import admin
from .models import (
    Country, Destination, Operator, OperatorDestination,
    Station, Route, RouteStation,
    Product, ProductVariant, ProductPricing, ProductImage,
    ProductInclusion, ProductTimetable, ProductDiscount,
    Booking, BookingItem, Payment
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


# ============================================
# PRODUCT ADMINS
# ============================================


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'operator', 'destination', 'product_type', 'status', 'duration_min']
    list_filter = ['product_type', 'status', 'destination__country']
    search_fields = ['name', 'description', 'operator__name']
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ['operator', 'destination']


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ['product', 'variant_name', 'variant_code', 'is_default', 'sort_order']
    list_filter = ['product__operator']


@admin.register(ProductPricing)
class ProductPricingAdmin(admin.ModelAdmin):
    list_display = ['product', 'variant', 'price_amount', 'currency', 'price_type', 'valid_from', 'is_active']
    list_filter = ['currency', 'price_type', 'is_active']
    raw_id_fields = ['product', 'variant']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'media_type', 'is_primary', 'sort_order']
    list_filter = ['media_type', 'is_primary']


@admin.register(ProductInclusion)
class ProductInclusionAdmin(admin.ModelAdmin):
    list_display = ['product', 'inclusion_type', 'category', 'description', 'sort_order']
    list_filter = ['inclusion_type', 'category']


@admin.register(ProductTimetable)
class ProductTimetableAdmin(admin.ModelAdmin):
    list_display = ['product', 'day_of_week', 'start_time', 'end_time', 'season']
    list_filter = ['day_of_week', 'season']


@admin.register(ProductDiscount)
class ProductDiscountAdmin(admin.ModelAdmin):
    list_display = ['product', 'discount_name', 'discount_type', 'discount_percent', 'is_active']
    list_filter = ['discount_type', 'is_active']


# ============================================
# BOOKING ADMINS
# ============================================


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['booking_reference', 'user', 'status', 'total_amount', 'currency', 'created_at']
    list_filter = ['status', 'currency', 'created_at']
    search_fields = ['booking_reference', 'user__email', 'contact_email']
    readonly_fields = ['booking_reference', 'created_at', 'updated_at']


@admin.register(BookingItem)
class BookingItemAdmin(admin.ModelAdmin):
    list_display = ['booking', 'product', 'variant', 'booking_date', 'quantity', 'total_price', 'status']
    list_filter = ['status', 'booking_date']
    raw_id_fields = ['booking', 'product', 'variant']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['booking', 'amount', 'currency', 'status', 'payment_method', 'paid_at']
    list_filter = ['status', 'payment_method', 'currency']
    readonly_fields = ['created_at']
