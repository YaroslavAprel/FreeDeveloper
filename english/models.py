from django.db import models

class Prices(models.Model):
	title = models.CharField(max_length = 35, verbose_name = "Название услуги")
	first_price = models.TextField(max_length = 10, verbose_name = "Цена 30 мин")
	two_price = models.TextField(max_length = 10, verbose_name = "Цена 45 мин")
	free_price = models.TextField(max_length = 10, verbose_name = "Цена 60 мин")
	four_price = models.TextField(max_length = 10, verbose_name = "Цена 90 мин")

	class Meta():
		verbose_name_plural = "Цены и услуги"
		verbose_name = "Цены и услуга"

