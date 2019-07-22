"""
Handles database interactions
"""
import sqlite3
from sqlite3 import Error

#connect to database
try:
    db = sqlite3.connect('transit_stops.db')
except Error as e:
    print (e)

#create cursor
cursor = db.cursor()

def get_stops_list(intersection_list):
    '''
    gets longitude, and latitude for each stop in list from the database, formats it for API request and returns
    a list of coordinates.
    '''
    for intersection in intersection_list:
        coordinates_list = []
        #replace 'and' with '&' because that is the way it is stored in the database.
        intersection = intersection.replace('and', '&')
        cursor.execute('select latitude from stops where intersection like ?', (intersection,))
        latitude = cursor.fetchone()
        cursor.execute('select longitude from stops where intersection like ?',(intersection,))
        longitude = cursor.fetchone()
        #coordinate = cursor.fetchone()
        coordinate = str(latitude) + ', ' + str(longitude)
        coordinates_list.append(coordinate)
        print(coordinate)

    return coordinates_list