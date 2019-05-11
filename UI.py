"""This class controls the user interface of the program as well as creates the window and widgets in the window."""

import tkinter as tk
from tkinter import ttk
from tkinter import *
import os 
import API_Manager


class MainWindow(Frame):

    """dictionary to hold the stop name and stop id so I can reference the stop id based on the stop name that is
    selected in the stop_menu"""
    STOP_INFO = {}

    def __init__(self, parent=None):
        Frame.__init__(self,parent)
        self.parent = parent
        self.create_widgets()
        self.pack()
        
        routes = API_Manager.get_routes()
        self.fill_routes(routes)
        


    def fill_routes(self, route_list):
        """method to fill the route_menu Combobox with available routes"""

        #fill with items from the list
        self.route_menu['values'] = route_list


    def fill_directions(self, direction_list):
        """method to fill the direction_menu combobox with available route directions"""

        #fill with items from the list
        self.direction_menu['values'] = direction_list


    def fill_stops(self, stop_dict):
        """method to fill stops_menu combobox with transit stops"""

        #list to hold the dictionary key stop names
        *stop_names, = stop_dict #idea from https://stackoverflow.com/questions/16819222/how-to-return-dictionary-keys-as-a-list-in-python/55448660#55448660

        #fill with items from the list
        self.stop_menu['values'] = stop_names


    def fill_departure_times(self, times_list):
        """method used to display departure times in the """

        self.departures_text.insert(END, f'Next departures are:\n')
        count = 0
        list_length = len(times_list)
        while count < list_length:
            self.departures_text.insert(END, times_list[count] + '\n')
            count += 1


    def convert_to_direction_code(self, direction):
        """method used to convert the text direction into a direction code for the Metro Transit API"""

        direction_code = ''
        if direction == 'NORTHBOUND':
            direction_code = '4'
        elif direction == 'SOUTHBOUND':
            direction_code = '1'
        elif direction == 'WESTBOUND':
            direction_code = '3'
        elif direction == 'EASTBOUND':
            direction_code = '2'

        return direction_code


    def create_widgets(self):
        """method used to create and pack widgets on the main window"""

        # set title
        self.parent.title('Metro Transit Departure Time Finder')

        #set icon
        self.parent.iconbitmap(os.path.join('assets', 'Bus_Stop.ico'))

        # set background image
        # todo get this working 
        photo = PhotoImage(os.path.join('assets', 'Capture.PNG'))
        photo_label = Label(self.parent, image=photo)
        photo_label.photo = photo
        photo_label.place(x=0, y=0, relwidth=1, relheight=1)

        # create frames
        self.button_frame = Frame(self.parent)
        self.map_frame = Frame(self.parent)

        #create labels for dropdown menus
        self.route_label = Label(self.button_frame, text='Select Your Route', bg='blue', fg='yellow')
        self.direction_label = Label(self.button_frame, text='Select Your Direction', bg='blue', fg='yellow')
        self.stop_label = Label(self.button_frame, text='Select Your Stop', bg='blue', fg='yellow')

        #create blank labels to space out things on window
        self.blank_label1 = Label(self.button_frame, text='  ')
        #self.blank_label2 = Label

        #create comboboxes
        self.route_menu = ttk.Combobox(self.button_frame, state='readonly', values=[])
        self.direction_menu = ttk.Combobox(self.button_frame, state='readonly', values=[])
        #start as disabled
        self.direction_menu.config(state=DISABLED)
        self.stop_menu = ttk.Combobox(self.button_frame, state='readonly', width=30, values=[])
        #start as disabled
        self.stop_menu.config(state=DISABLED)

        #create button
        self.go_button = Button(self.button_frame, text='GO!', bg='blue', fg='yellow')
        self.go_button.config(state=DISABLED)

        #create Text field for departure times
        self.departures_text = Text(self.map_frame, width=20, height=20)

        #pack contents
        self.button_frame.pack(side=LEFT)
        self.map_frame.pack(side=RIGHT)
        self.route_label.grid(row=0, column=2, sticky=S)
        self.route_menu.grid(row=1, column=2)
        self.direction_label.grid(row=2, column=2, sticky=S)
        self.direction_menu.grid(row=3, column=2)
        self.stop_label.grid(row=4, column=2, sticky=S)
        self.stop_menu.grid(row=5, column=2)
        self.go_button.grid(row=6, column=2)
        self.departures_text.grid(row=0, column=0)

        """event handlers"""

        def route_selected(event):
            """This handler gets the directions of a route after a route has been selected from the route_menu combobox
            and puts them in the direction_menu combobox"""

            #get selected items
            route = self.route_menu.get()
            directions = API_Manager.get_directions(route)
            #enable direction_menu combobox
            self.direction_menu.config(state=ACTIVE)
            #clear the combobox selections
            self.direction_menu.set('')
            self.stop_menu.set('')
            #clear the Text area
            self.departures_text.delete(1.0, END)
            #disable stops_menu combobox and go_button
            self.stop_menu.config(state=DISABLED)
            self.go_button.config(state=DISABLED)
            #populate the combobox with the response data
            self.fill_directions(directions)


        def direction_selected(event):
            """This handler gets the stops after a direction has been selected from the direction_menu combobox and puts them
            in the stop_menu combobox"""

            #get selected items
            route = self.route_menu.get()
            direction = self.direction_menu.get()

            #convert combobox text to a direction code for api
            direction_code = self.convert_to_direction_code(direction)

            #get the data from Metro Transit API
            self.STOP_INFO = API_Manager.get_stops(route, direction_code)

            #enable the stop_menu combobox
            self.stop_menu.config(state=ACTIVE)
            #disable go_button
            self.go_button.config(state=DISABLED)
            #clear the stop_menu combobox selection
            self.stop_menu.set('')
            self.fill_stops(self.STOP_INFO)
            #clear Text area
            self.departures_text.delete(1.0, END)


        def stop_selected(event):
            """This handler enables the go_button after the stop is selected"""

            #enable go_button
            self.go_button.config(state=ACTIVE)
            #clear Text area
            self.departures_text.delete(1.0, END)


        def go_pressed(event):
            """This handler gets the departure times and map when the go button has been pressed"""

            #get selected info
            route = self.route_menu.get()
            direction = self.direction_menu.get()
            stop = self.stop_menu.get()
            #convertthe direction into the direction code
            direction_code = self.convert_to_direction_code(direction)
            #reference the STOP_INFO dictionary to get stop id from the selected stop name
            stop_id = self.STOP_INFO[stop]
            #get departure times from Metro Transit
            times = API_Manager.get_times(route, direction_code, stop_id)

            #get map from Google Maps

            # clear Text area
            self.departures_text.delete(1.0, END)
            #fill departures_text with departure times
            self.fill_departure_times(times)

            #display map on ui


        #bind widgets to event handlers
        self.route_menu.bind("<<ComboboxSelected>>", route_selected)
        self.direction_menu.bind("<<ComboboxSelected>>", direction_selected)
        self.stop_menu.bind("<<ComboboxSelected>>", stop_selected)
        self.go_button.bind("<Button-1>", go_pressed)


def main():
    root = Tk()
    main_window = MainWindow(root)
    root.mainloop()


main()
