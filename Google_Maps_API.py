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
    marker_string = 'size:mid|color:red'
    for point in intersection_list:
        marker_list.append(point)
    print(marker_list)
    return marker_list


def build_visible_string(intersection_list):
    """Builds visible points for each stop intersection for the map to display"""

    #process each stop/intersection in the correct for to be visible on the map and add to visible_String
    visible_string = ''
    for stop in intersection_list:
        #replace spaces
        stop = stop.replace(' ', '%20')
        #add formatting to visible
        stop = stop + '%7C'
        visible_string += stop
    # removing last space characters
    visible_string = visible_string.strip('%7C')

    return visible_string


def get_map(marker_list, visible_list, key):
    #setup parameters for the api query
    #todo finish list of desired parameters
    parameters = {'size': '900x900', 'format': 'gif', 'markers': marker_list, 'visible': visible_list,'key': key}
    response = make_request(parameters, map_url)
    return response


def make_request(parameters, map_url):
    #request data from google maps
    try:
        response = requests.get(map_url, params=parameters)
        #raise error is certain response codes are returned
        response.raise_for_status()
        return response
    except HTTPError as http_err:
        print(f'HTTP error: {http_err}')
    except Exception as ex:
        print(f'Other error: {ex}')
