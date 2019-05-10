"""
High-level management of APIs

Connects to Metro Transit and Google Maps static map API 

"""
import os
import Metro_Transit_API
import Google_Maps_API
# import UI

#get api key from the os
maps_key = os.environ.get('GoogleMapsKey')

#instantiate instances of APIs
# metroTransit = Metro_Transit_API
# googleMaps = Google_Maps_API

#instantiate instance of UI
# ui = UI

def get_routes():
    """ Fetches all the Metro Transit route numbers for buses and trains """ 
    response = Metro_Transit_API.get_routes()
    route_numbers = route_numbers_from_response(response)
    return route_numbers


def route_numbers_from_response(response):
    """extracts route numbers from the response and returns as a list"""
    #list to hold route numbers
    route_numbers = []
    for route in response:
        route_numbers.append(route['Route'])
    #fill combobox with route numbers
    return route_numbers


def get_directions(route_number):
    """Fetches directions of selected route from the Metro Transit API"""
    response = Metro_Transit_API.get_direction(route_number)
    directions = directions_from_response(response)
    return directions


def directions_from_response(response):
    """extracts the directions from the response and returns a list"""
    #list to hold route directions
    directions = []
    for direction in response:
        directions.append(direction['Text'])
    return directions

#method to get the stops for the route and selected direction
def get_stops(route_num, direction):
    """Fetches the  stops for a selected route and direction from the Metro Transit API"""
    response = Metro_Transit_API.get_stops(route_num, direction)
    stops = stops_from_response(response)
    return stops

def stops_from_response(response):
    """Extracts the stops from the response and returns as a list"""
    #list to hold stops
    stops = []
    for stop in response:
        stops.append(stop['Text'])
    return stops

'''#method to get the stop times
def get_times():


#method to get the map
def get_map():
'''