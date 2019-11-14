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
        self.heading_label.place(x=20, y=25)
        
        #style component 
        self.heading_label.configure(text="RECIEVE OUR NEWSLETTER", 
                                     font="Arial 15",
                                     fg="#000",
                                     bg="#FFF")

        #add event handling to the component 
    
    def add_message_label(self):
        #create the component
        self.message_label = Label()
        self.message_label.place(x=39, y=80)
        
        #style component 
        self.message_label.configure(text="Please enter your email below to recieve our newsletter", 
                                     font="Arial 8")
                                    
    def add_enter_label(self):
        #create the component
        self.enter_label = Label()
        self.enter_label.place(x=40, y=120)
        
        #style component 
        self.enter_label.configure(text="Email:", 
                                     font="Arial 8")


    def add_button_label(self):
        #create the component
        self.button_label = Button()
        self.button_label.place(x=50, y=150,
        height=35, width=440)
        self.button_label.configure(text="Subscribe")
    
    def add_entry_label(self):
        #create the component
        self.entry_label = Entry()
        self.entry_label.place(x=95, y=120,
        height=25, width=350)
