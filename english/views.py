from django.shortcuts import render
from .models import Prices

def index(request):
	prices = Prices.objects.all()
	return render(request, 'english/index.html', { "prices":prices })


def by_about_us(request):
	prices = Prices.objects.all()
	return render(request, "english/2016.html", { "prices":prices })


def by_price(request):
	prices = Prices.objects.all()
	return render(request, "english/foto.html", { "prices":prices })


def by_reviews(request):
	prices = Prices.objects.all()
	return render(request, "english/teachers.html", { "prices":prices })

def by_contacts(request):
	prices = Prices.objects.all()
	return render(request, "english/contacts.html", { "prices":prices })

# Create your views here.
