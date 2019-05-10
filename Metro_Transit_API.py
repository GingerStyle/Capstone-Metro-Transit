import requests
from requests.exceptions import HTTPError

#urls for reqests
PARAMETERS = {'format': 'json'}
routeUrl = "http://svc.metrotransit.org/NexTrip/Routes"
directionUrl = "http://svc.metrotransit.org/NexTrip/Directions/"
stopsUrl = "http://svc.metrotransit.org/NexTrip/Stops/"
departTimeUrl = "http://svc.metrotransit.org/NexTrip/"


#method to build url to get routes
def get_routes():
    url = routeUrl
    #call get_data to make request
    response = get_data(url, PARAMETERS)
    return response


#method to build url to get route directions for specific route
def get_direction(route_num):
    url = directionUrl + '/' + route_num
    #call get_data to make request
    response = get_data(url, PARAMETERS)
    return response


#method to build url to get stops from specific route and direction
def get_stops(route_num, direction):
    url = stopsUrl + '/' + route_num + '/' + direction
    #call get_data to make request
    response = get_data(url, PARAMETERS)
    return response


#method to build url to get departure times for specific stop, route, and direction
def get_times(route, direction, stop):
    url = departTimeUrl + '/' + route + '/' + direction + '/' + stop
    #call get_data to make request
    response = get_data(url, PARAMETERS)
    return response


#method to use built urls to get data from metro transit
def get_data(url, parameters):
    #request data from metro transit
    try:
        response = requests.get(url, params=parameters)
        #raise error if certain response codes are returned
        response.raise_for_status()

        return response.json() 
        
    except HTTPError as http_err:
        print(f'HTTP error: {http_err}')
    except Exception as ex:
        print(f'Other error: {ex}')

