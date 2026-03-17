from django.db import models


class Location(models.Model):
	name = models.CharField(max_length=150, unique=True)
	is_terminal = models.BooleanField(default=True, help_text="Marca si es una terminal principal")

	class Meta:
		verbose_name = "Ubicación"
		verbose_name_plural = "Ubicaciones"
		ordering = ["name"]

	def __str__(self) -> str:
		return self.name


class Route(models.Model):
	origin = models.CharField(max_length=100)
	destination = models.CharField(max_length=100)
	estimated_duration = models.DurationField(help_text="Duración estimada del viaje")
	image = models.ImageField(upload_to="routes/", blank=True, null=True)

	class Meta:
		verbose_name = "Ruta"
		verbose_name_plural = "Rutas"

	def __str__(self) -> str:
		return f"{self.origin} 	 {self.destination}"


class Vehicle(models.Model):
	bus_number = models.CharField(max_length=20, unique=True)
	capacity = models.PositiveIntegerField()
	has_wifi = models.BooleanField(default=True)
	has_air_conditioning = models.BooleanField(default=True)

	class Meta:
		verbose_name = "Vehículo"
		verbose_name_plural = "Vehículos"

	def __str__(self) -> str:
		return f"Bus {self.bus_number} (Capacidad {self.capacity})"


class Schedule(models.Model):
	route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="schedules")
	vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="schedules")
	departure_time = models.DateTimeField()
	price = models.DecimalField(max_digits=10, decimal_places=2)

	class Meta:
		verbose_name = "Horario"
		verbose_name_plural = "Horarios"
		ordering = ["departure_time"]

	def __str__(self) -> str:
		return f"{self.route} - {self.departure_time:%Y-%m-%d %H:%M}"


class Banner(models.Model):
	title = models.CharField(max_length=150)
	image = models.FileField(upload_to="banners/")
	link = models.URLField(blank=True)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Banner publicitario"
		verbose_name_plural = "Banners publicitarios"
		ordering = ["-created_at"]

	def __str__(self) -> str:
		return self.title
