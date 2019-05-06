import Metro_Transit_API


#instantiate instances of APIs
metroTransit = Metro_Transit_API


#variables to hold response
METRO_RESPONSE = []


def get_routes():
    route = 'route'
    
    response = metroTransit(route)
