import requests
from requests.exceptions import HTTPError

#urls for reqests
formatLine = "?format=json"
routeUrl = "http://svc.metrotransit.org/NexTrip/Routes"
directionUrl = "http://svc.metrotransit.org/NexTrip/Directions/"
stopsUrl = "http://svc.metrotransit.org/NexTrip/Stops/"
departTimeUrl = "http://svc.metrotransit.org/NexTrip/"

def get_data(operation):
    Url = ''
    if operation == 'route':
        Url = routeUrl + formatLine
    elif operation == 'direction':
        Url = directionUrl + formatLine
    elif operation == 'stops':
        Url = stopsUrl + formatLine
    elif operation == 'departure':
        Url = departTimeUrl + formatLine

    #request data from metro transit
    try:
        response = requests.get(Url)
        #raise error if certain response codes are returned
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error: {http_err}')
    except Exception as ex:
        print(f'Other error: {ex}')
    else:
        return response


#todo create method to cross reference addresses to get five digit stop id
