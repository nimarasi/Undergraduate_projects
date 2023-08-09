"""
I have added this urls.py file to /art_app/

this file will manage app urls

the urls.py file in /django_project/urls.py will manage whole project urls
"""
from django.urls import path
from . import views


# this list will cheked by django that if request come to certain url what should do

urlpatterns = [ path("" , views.starting_page ), # our-domain.com/starting_page 
                path("starting_page/" , views.starting_page),
                path("starting_page/art_fields", views.art_fields, name='all-fields'),# our-domain.com/starting_page/art_fields
                path("starting_page/art_fields/<slug:field_detail>" , views.fields_detail , name='field-detail') # our-domain.com/starting_page/<dynamic-path-segment>
                ]