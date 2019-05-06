import os
import Metro_Transit_API
import Google_Maps_API
import UI

#get api key
maps_key = os.environ.get('GoogleMapsKey')

#instantiate instances of APIs
metroTransit = Metro_Transit_API
googleMaps = Google_Maps_API

#variables to hold response
METRO_RESPONSE = []


#method to take routes and return to main controller as dictionary
def get_routes():
    #get routes
    response = metroTransit.get_routes()
    #put response into dictionary
    #todo figure out how to reference list with no name
    routes = response[]
    #todo put routes into drop down box on UI

#method to get the directions for the route
def get_directions():


#method to get the stops for the route and selected direction
def get_stops():


#method to get the stop times
def get_times():


#method to get the map
def get_map():
