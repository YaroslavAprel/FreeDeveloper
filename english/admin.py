from django.contrib import admin
from .models import Prices

class adminPrices(admin.ModelAdmin):
	list_display = ("title", "first_price", "two_price", "free_price", "four_price")
	list_display_links = ("title", "first_price", "two_price", "free_price", "four_price")

admin.site.register(Prices, adminPrices)

