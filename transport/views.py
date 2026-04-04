from django.views.generic import TemplateView, DetailView
from django.db.models import Min
from django.conf import settings

from .models import Banner, Route, Location


class HomeView(TemplateView):
	template_name = "transport/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["active_banners"] = Banner.objects.filter(is_active=True)
		context["featured_routes"] = (
			Route.objects.annotate(min_price=Min("schedules__price")).all()[:6]
		)
		context["locations"] = Location.objects.all()
		return context

class RouteDetailView(DetailView):
	model = Route
	template_name = "transport/route_detail.html"
	context_object_name = "route"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		route = self.get_object()
		
		# Intentar buscar las Locations por nombre para obtener coordenadas
		origin_location = Location.objects.filter(name__iexact=route.origin).first()
		destination_location = Location.objects.filter(name__iexact=route.destination).first()
		
		map_data = {
			"origin": None,
			"destination": None
		}

		if origin_location and origin_location.latitude and origin_location.longitude:
			map_data["origin"] = {"lat": origin_location.latitude, "lng": origin_location.longitude}
		
		if destination_location and destination_location.latitude and destination_location.longitude:
			map_data["destination"] = {"lat": destination_location.latitude, "lng": destination_location.longitude}
			
		context["map_data"] = map_data
		context["GOOGLE_MAPS_API_KEY"] = getattr(settings, 'GOOGLE_MAPS_API_KEY', 'YOUR_API_KEY')
		return context
