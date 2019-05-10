import UI
from UI import MainWindow
import tkinter as tk

import API_Manager

def main():

    #get the currently running routes
    routes = API_Manager.get_routes()


main()