from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Tickets")
    
        
        # add components
        self.add_heading_label()
        self.add_instruction_label()
        self.add_tickets_entry()
        self.add_buy_button()
        
    def add_heading_label(self):
        #create
        self.heading_label = Label()
        self.heading_label.grid(row = 0, column = 0, ipadx = 20, ipady = 20)
        #style
        self.heading_label.configure(text = "Entrance Ticket",
                                    font = "Arial 24",
                                    fg = "#000",
                                    bg = "#FFF")
        
    def add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.configure(text = "How many tickets are needed?",
                                        font = "Arial 16",
                                        fg = "#000",
                                        bg = "#FFF")
        self.instruction_label.grid(row = 1, column = 0, sticky = W, ipadx = 10, ipady = 10)
        
    def add_tickets_entry(self):
        self.tickets_entry = Entry()
        self.tickets_entry.grid(row = 2, column = 0)
        
    def add_buy_button(self):
        self.buy_button = Button()
        self.buy_button.configure(text = "Buy")
        self.buy_button.grid(row = 3, column = 0)