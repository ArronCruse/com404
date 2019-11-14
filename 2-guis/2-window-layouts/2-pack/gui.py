from tkinter import*


class Gui(Tk):
    
    # constructor to cionstruct Gui objects 
    def __init__(self):
        super().__init__()

        #set window attributes 
        self.configure (
                        height=175,
                        width=337)
        self.title ("Newsletter")
        
        #add window components 
        self.add_heading_label()
        self.add_message_label()
        self.add_enter_label()
        self.add_button_label() 
        self.add_entry_label()

    #methods
    def add_heading_label(self):
        #create the component
        self.heading_label = Label()
        self.heading_label.grid(row = 2, column = 0, columnspan = 2)
        
        #style component 
        self.heading_label.configure(text="RECIEVE OUR NEWSLETTER", 
                                     font="Arial 15",
                                     fg="#000",
                                     bg="#FFF")

        #add event handling to the component 
    
    def add_message_label(self):
        #create the component
        self.message_label = Label()
        self.message_label.grid(row = 3, column = 0, columnspan = 2)
        
        #style component 
        self.message_label.configure(text="Please enter your email below to recieve our newsletter", 
                                     font="Arial 8")
        #create the component                            
    def add_enter_label(self):
        
        self.enter_label = Label()
        self.enter_label.grid(row = 4, column = 0)
        
        #style component 
        self.enter_label.configure(text="Email:", 
                                     font="Arial 8")


    def add_button_label(self):
        #create the component
        self.button_label = Button()
        self.button_label.grid(row = 5, column = 0, columnspan = 2)
        self.button_label.configure(text="Subscribe")
    
    def add_entry_label(self):
        #create the component
        self.entry_label = Entry()
        self.entry_label.grid(row = 4, column = 1)