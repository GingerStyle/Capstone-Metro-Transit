import tkinter as tk
from tkinter import ttk
from tkinter import *
import os 
import API_Manager

class MainWindow(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self,parent)
        self.parent = parent
        self.create_widgets()
        self.pack()
        
        routes = API_Manager.get_routes()
        self.fill_routes(routes)
        # todo add routes to route_menu 
        

    #method to fill the route_menu OptionMenu with available routes
    def fill_routes(self, route_list):
        #fill with items from the list
        self.route_menu['values'] = route_list


    def create_widgets(self):
        # set title
        self.parent.title('Metro Transit Departure Time Finder')

        #set icon
        self.parent.iconbitmap(os.path.join('assets', 'Bus_Stop.ico'))

        # set background image
        # todo get this working 
        photo = PhotoImage(r'C:\Users\myles\PycharmProjects\MetroTransit\Capture.PNG')  # fix this path too
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

        #create comboboxes
        #todo create lists to store API responses to fill OptionMenus
        self.route_menu = ttk.Combobox(self.button_frame, state='readonly', values=[])
        self.direction_menu = ttk.Combobox(self.button_frame, state='readonly', values=[])
        self.stop_menu = ttk.Combobox(self.button_frame, state='readonly', values=[])

        #create button
        self.go_button = Button(self.button_frame, text='GO!', bg='blue', fg='yellow')

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


def main():
    root = Tk()
    main_window = MainWindow(root)
    root.mainloop()


main()
