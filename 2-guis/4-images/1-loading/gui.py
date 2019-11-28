from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.ambulance_image = PhotoImage(file="U:\\com404\\2-guis\\4-images\\ambulance.gif")
        self.bike_image = PhotoImage(file="U:\\com404\\2-guis\\4-images\\bike.gif")
        self.plane_image = PhotoImage(file="U:\\com404\\2-guis\\4-images\\plane.gif")
        # set window attributes
        self.configure (
                        height=175,
                        width=337)
        self.title ("GUI")
        
        # add components
        self.add_heading_label()
        self.__add_ambulance_image_label()
        self.__add_bike_image_label()
        self.__add_plane_image_label()

    def add_heading_label(self):
        #create the component
        self.heading_label = Label()
        self.heading_label.grid(row = 0, column = 0, columnspan = 3)

        self.heading_label.configure(text="Transport", 
                                     font="Arial 24")

    def __add_ambulance_image_label(self):
        self.ambulance_image_label = Label()
        self.ambulance_image_label.grid(row=1, column=0)
        self.ambulance_image_label.configure(image=self.ambulance_image,
                                             height=60,
                                             width=60)

    def __add_bike_image_label(self):
        self.bike_image_label = Label()
        self.bike_image_label.grid(row=1, column=1)
        self.bike_image_label.configure(image=self.bike_image,
                                             height=60,
                                             width=60)
 
    def __add_plane_image_label(self):
        self.plane_image_label = Label()
        self.plane_image_label.grid(row=1, column=2)
        self.plane_image_label.configure(image=self.plane_image,
                                             height=60,
                                             width=60)
 

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()