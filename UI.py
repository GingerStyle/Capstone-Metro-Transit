import tkinter as tk
from tkinter import ttk
from tkinter import *
import os 
import API_Manager

"""This class controls the user interface of the program as well as creates the window and widgets in the window."""
class MainWindow(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self,parent)
        self.parent = parent
        self.create_widgets()
        self.pack()
        
        routes = API_Manager.get_routes()
        self.fill_routes(routes)
        

    """method to fill the route_menu Combobox with available routes"""
    def fill_routes(self, route_list):
        #fill with items from the list
        self.route_menu['values'] = route_list

    """method to fill the direction_menu combobox with available route directions"""
    def fill_directions(self, direction_list):
        self.direction_menu['values'] = direction_list

    """method to fill stops_menu combobox with transit stops"""
    def fill_stops(self, stop_list):
        self.stop_menu['values'] = stop_list

    """method used to create and pack widgets on the main window"""
    def create_widgets(self):
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
        #todo create lists to store API responses to fill OptionMenus
        self.route_menu = ttk.Combobox(self.button_frame, state='readonly', values=[])
        self.direction_menu = ttk.Combobox(self.button_frame, state='readonly', values=[])
        #start as disabled
        self.direction_menu.config(state=DISABLED)
        self.stop_menu = ttk.Combobox(self.button_frame, state='readonly', values=[])
        #start as disabled
        self.stop_menu.config(state=DISABLED)

        #create button
        self.go_button = Button(self.button_frame, text='GO!', bg='blue', fg='yellow')
        self.go_button.config(state=DISABLED)

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

        """event handlers"""
        """This handler gets the directions of a route after a route has been selected from the route_menu combobox
        and puts them in the direction_menu combobox"""
        def route_selected(event):
            #get selected item
            route = self.route_menu.get()
            directions = API_Manager.get_directions(route)
            #enable direction_menu combobox
            self.direction_menu.config(state=ACTIVE)
            #clear the combobox selections
            self.direction_menu.set('')
            self.stop_menu.set('')
            #disable stops_menu combobox
            self.stop_menu.config(state=DISABLED)
            #populate the combobox with the response data
            self.fill_directions(directions)

        """This handler gets the stops after a direction has been selected from the direction_menu combobox and puts them
        in the stop_menu combobox"""
        def direction_selected(event):
            route = self.route_menu.get()
            direction = self.direction_menu.get()
            #convert text to direction code for api
            direction_code = ''
            if direction == 'NORTHBOUND':
                direction_code = '4'
            elif direction == 'SOUTHBOUND':
                direction_code = '1'
            elif direction == 'WESTBOUND':
                direction_code = '3'
            elif direction == 'EASTBOUND':
                direction_code = '2'

            stops = API_Manager.get_stops(route, direction_code)
            #enable the stop_menu combobox
            self.stop_menu.config(state=ACTIVE)
            #clear the stop_menu combobox selection
            self.stop_menu.set('')
            self.fill_stops(stops)

        """This handler gets the departure times and map when the go button has been pressed"""
        def go_pressed(event):
            route = self.route_menu.get()
            direction = self.direction_menu.get()
            stop = self.stop_menu.get()

        #bind widgets to event handlers
        self.route_menu.bind("<<ComboboxSelected>>", route_selected)
        self.direction_menu.bind("<<ComboboxSelected>>", direction_selected)
        self.go_button.bind("<Button-1>", go_pressed)




def main():
    root = Tk()
    main_window = MainWindow(root)
    root.mainloop()


main()
