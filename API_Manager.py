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


def build_marker_list(intersection_list):
    """Builds marker points for each stop intersection for the map to display"""

    #process each stop/intersection in the correct form as a marker and add to marker_string
    marker_list = []
    marker_string = 'size:small|color:red|'
    for point in intersection_list:
        point = marker_string + point
        marker_list.append(point)

    return marker_list


def build_visible_list(intersection_list):
    """Takes the first and last stop on the route and add to a list used to make sure they are both visible on the map."""

    #process each stop/intersection in the correct for to be visible on the map and add to visible_String
    visible_list = []
    visible_list.append(intersection_list[0])
    visible_list.append(intersection_list[len(intersection_list) - 1])

    return visible_list

def get_map_center(intersection_list):
    """takes the middle stop on the route and uses it for the center of the map"""

    list_middle = len(intersection_list) / 2
    map_center = intersection_list[int(list_middle)]

    return map_center


def get_map(intersection_list):
    """Sends intersection_list to build strings for the markers and visible parameters then get the map and save to a file"""

    marker_list = build_marker_list(intersection_list)
    visible_list = build_visible_list(intersection_list)
    map_center = get_map_center(intersection_list)
    map = Google_Maps_API.get_map(marker_list, visible_list, map_center, maps_key)

    #save map to file
    with open('map.gif', 'wb') as map_gif:
        for chunk in map.iter_content():
            map_gif.write(chunk)

