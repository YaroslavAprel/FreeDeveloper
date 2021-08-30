
from django.urls import path
from .views import index, by_price, by_contacts, by_about_us, by_reviews


urlpatterns = [
    path('', index, name = 'index'),
    path('about_us', by_about_us, name = 'by_about_us'),
    path('price', by_price, name = 'by_price'),
    path('reviews', by_reviews, name = 'by_reviews'),
    path('contacts', by_contacts, name = 'by_contacts'),
]
