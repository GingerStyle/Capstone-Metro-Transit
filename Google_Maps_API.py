"""
Stores url information and connection method for the Google Maps Static Map API
"""

import requests
from requests.exceptions import HTTPError

map_url = 'https://maps.googleapis.com/maps/api/staticmap'

class Google_Map_API():

    def get_map(self, key):
        #setup parameters for the api query
        #todo setup to handle different quantities of stops
        #todo finish list of desired parameters
        parameters = {'size': '900x900', 'zoom': '13', 'center': 'Minneapolis,MN', 'format': 'gif', 'key': key}
        response = self.make_request(parameters, map_url)
        return response

    def make_request(self, parameters, map_url):
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
