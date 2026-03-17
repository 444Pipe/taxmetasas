from django.contrib import admin

from .models import Banner, Route, Vehicle, Schedule, Location
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
	list_display = ("name", "is_terminal")
	list_filter = ("is_terminal",)
	search_fields = ("name",)



@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
	list_display = ("title", "is_active", "created_at")
	list_filter = ("is_active", "created_at")
	search_fields = ("title",)


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
	list_display = ("origin", "destination", "estimated_duration")
	search_fields = ("origin", "destination")


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
	list_display = ("bus_number", "capacity", "has_wifi", "has_air_conditioning")
	list_filter = ("has_wifi", "has_air_conditioning")
	search_fields = ("bus_number",)


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
	list_display = ("route", "vehicle", "departure_time", "price")
	list_filter = ("route", "vehicle", "departure_time")
