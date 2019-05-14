"""
Stores url information and connection method for the Google Maps Static Map API
"""

import requests
from requests.exceptions import HTTPError

map_url = 'https://maps.googleapis.com/maps/api/staticmap'


def build_marker_string(intersection_list):
    """Builds marker points for each stop intersection for the map to display"""

    #process each stop/intersection in the correct form as a marker and add to marker_string
    marker_list = []
    marker_string = 'size:mid|color:red|'
    for point in intersection_list:
        point = marker_string + point
        marker_list.append(point)

    return marker_list


def build_visible_string(intersection_list):
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


def get_map(marker_list, visible_list, map_center, key):
    #setup parameters for the api query
    parameters = {'size': '900x900', 'format': 'gif', 'center': map_center,'markers': marker_list, 'visible': visible_list,'key': key}
    response = make_request(parameters, map_url)
    return response


def make_request(parameters, map_url):
    #request data from google maps
    try:
        response = requests.get(map_url, params=parameters, stream=True)
        #raise error is certain response codes are returned
        response.raise_for_status()
        return response
    except HTTPError as http_err:
        print(f'HTTP error: {http_err}')
    except Exception as ex:
        print(f'Other error: {ex}')
