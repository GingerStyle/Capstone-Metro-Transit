"""
Stores url information and connection method for the Google Maps Static Map API
"""

import requests
from requests.exceptions import HTTPError

map_url = 'https://maps.googleapis.com/maps/api/staticmap'


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
