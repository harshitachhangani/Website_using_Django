from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path("", views.index, name='home'),
   path("about", views.about, name='about'),
   path("services", views.services, name='services'),
   path("contact", views.contact, name='contact'),
   path("explore", views.explore, name='explore'),
   path("risk", views.risk, name='risk'),
   path("hazard", views.hazard, name='hazard'),
   path("genelab", views.genelab, name='genelab'),
   path("space_bio_pro", views.space_bio_pro, name='space_bio_pro'),
]