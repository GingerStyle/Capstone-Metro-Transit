"""
High-level management of APIs

Connects to Metro Transit and Google Maps static map API 

"""
import os
import Metro_Transit_API
import Google_Maps_API
import base64


#get api key from the os
maps_key = os.environ.get('GoogleMapsKey')

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


def get_stops(route_num, direction):
    """Fetches the  stops for a selected route and direction from the Metro Transit API"""

    response = Metro_Transit_API.get_stops(route_num, direction)
    stops = stops_from_response(response)
    return stops


def stops_from_response(response):
    """Extracts the stops and ids from the response and returns a dictionary with the stop
    as the key and the stop id as the value"""

    #list to hold stops
    stops = {}
    for stop in response:
        dict_entry = {stop['Text']: stop['Value']}
        stops.update(dict_entry)
    return stops


def get_times(route_num, direction, stop_id):
    """Fetches departure times for the given route, direction, and specific stop form Metro Transit"""

    response = Metro_Transit_API.get_times(route_num, direction, stop_id)
    times = times_from_response(response)
    return times


def times_from_response(response):
    """Extracts departure times from the response and returns as a string"""

    #list to hold departure times
    times = []
    for time in response:
        times.append(time['DepartureText'])
    return times


def get_map(intersection_list):
    """Sends intersection_list to build strings for the markers and visible parameters then get the map and save to a file"""

    marker_list = Google_Maps_API.build_marker_string(intersection_list)
    visible_list = Google_Maps_API.build_visible_string(intersection_list)
    map_center = Google_Maps_API.get_map_center(intersection_list)
    map = Google_Maps_API.get_map(marker_list, visible_list, map_center, maps_key)
    #save map to file
    open("map_gif.txt", "w+")
    with open('map_gif.txt', 'wb') as fd:
        for chunk in map.iter_content(chunk_size=128):
            fd.write(chunk)
    """
    with open('map_gif.txt', 'rb') as imagefile:
        base64string = base64.b64encode(imagefile.read()).decode('ascii')
    print(base64string)
    with open('map_gif.txt', 'w') as outputfile:
        outputfile.write(base64string)
    gif_file.close()
"""
    #return map