import tkinter as tk
from tkinter import ttk
from tkinter import *

class MainWindow(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self,parent)
        self.parent = parent
        self.pack()

    #method to fill the route_menu OptionMenu with available routes
    def fill_routes(self, route_list):
        #fill with items from the list
        route_menu['values'] = route_list


root = Tk()

#set title
root.title('Metro Transit Departure Time Finder')

#set icon
root.iconbitmap(r'C:\Users\myles\PycharmProjects\MetroTransit\Bus_Stop.ico')

#set background image
#todo get this working
photo = PhotoImage(r'C:\Users\myles\PycharmProjects\MetroTransit\Capture.PNG')
photo_label = Label(root, image=photo)
photo_label.photo = photo
photo_label.place(x=0, y=0, relwidth=1, relheight=1)

#create frames
button_frame = Frame(root)
map_frame = Frame(root)

#create labels for dropdown menus
route_label = Label(button_frame, text='Select Your Route', bg='blue', fg='yellow')
direction_label = Label(button_frame, text='Select Your Direction', bg='blue', fg='yellow')
stop_label = Label(button_frame, text='Select Your Stop', bg='blue', fg='yellow')

#create comboboxes
#todo create lists to store API responses to fill OptionMenus
route_menu = ttk.Combobox(button_frame, state='readonly', values=[])
direction_menu = ttk.Combobox(button_frame, state='readonly', values=[])
stop_menu = ttk.Combobox(button_frame, state='readonly', values=[])

#create button
go_button = Button(button_frame, text='GO!', bg='blue', fg='yellow')

#pack contents
button_frame.pack(side=LEFT)
map_frame.pack(side=RIGHT)
route_label.grid(row=0, column=2, sticky=S)
route_menu.grid(row=1, column=2)
direction_label.grid(row=2, column=2, sticky=S)
direction_menu.grid(row=3, column=2)
stop_label.grid(row=4, column=2, sticky=S)
stop_menu.grid(row=5, column=2)
go_button.grid(row=6, column=2)


main_window = MainWindow(root)
root.mainloop()
