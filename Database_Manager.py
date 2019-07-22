"""
Handles database interactions
"""
import sqlite3

#connect to database
db = sqlite3.connect('transit_stops.db')

#create cursor
cursor = db.cursor()

def get_stops_list(intersection_list):
    '''
    gets longitude, and latitude for each stop in list from the database, formats it for API request and returns
    a list of coordinates.
    '''
    for intersection in intersection_list:
        coordinates = []
        latitude = cursor.execute(f'select latitude_text from stops where intersection_text like {intersection}')
        longitude = cursor.execute(f'select longitude_text from stops where intersection_text like {intersection}')
        coordinate = latitude + ', ' + longitude
        coordinates.append(coordinate)

    return coordinates