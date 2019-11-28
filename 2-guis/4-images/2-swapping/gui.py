from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.osrs_image = PhotoImage(file="U:\\com404\\2-guis\\4-images\\2-swapping\\osrs_image.png")
        self.osrss_image = PhotoImage(file="U:\\com404\\2-guis\\4-images\\2-swapping\\osrss.gif")
        # set window attributes
        self.configure (
                        height=175,
                        width=337,
                        bg = "#000")
        self.title ("GUI")
        
        # add components
        self.add_heading_label()
        self.add_osrs_image_label()
        self.add_button_label()

    def add_heading_label(self):
        #create the component
        self.heading_label = Label()
        self.heading_label.grid(row = 0, column = 0, columnspan = 3)

        self.heading_label.configure(text="Git gud skrub", 
                                     font="Arial 24",
                                     fg = "#FF0",
                                     bg = "#000")
    
    def add_osrs_image_label(self):
        self.osrs_image_label = Label()
        self.osrs_image_label.grid(row=1, column=0)
        self.osrs_image_label.configure(image=self.osrs_image,
                                             height=936,
                                             width=425)

    
    def add_button_label(self):
        #create the component
        self.button_label = Button()
        self.button_label.grid(row = 5, column = 0, columnspan = 5)
        self.button_label.configure(text="flip")
        self.button_label.bind("<ButtonRelease-1>", self.button_label_clicked)
        self.button_label.bind("<ButtonRelease-3>", self.button_label_clickered)

    def button_label_clicked(self, event):
        self.osrs_image_label.configure(image=self.osrs_image)

    def button_label_clickered(self, event):
        self.osrs_image_label.configure(image=self.osrss_image)
 

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()