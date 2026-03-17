from django.views.generic import TemplateView
from django.db.models import Min

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
