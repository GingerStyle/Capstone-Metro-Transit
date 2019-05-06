import requests
from requests.exceptions import HTTPError

map_url = 'https://maps.googleapis.com/maps/api/staticmap?'

class Google_Map_API():

    def get_map(self, center, key):
        #setup parameters for the api query
        #todo setup to handle different quantities of stops
        #todo finish list of desired parameters
        parameters = {'center': 'center', 'key': {key}}

        #request data from google maps
        try:
            response = requests.get(map_url, params=parameters)
            #raise error is certain response codes are returned
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error: {http_err}')
        except Exception as ex:
            print(f'Other error: {ex}')
        else:
            return response