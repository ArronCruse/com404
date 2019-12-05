from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.cup1_image = PhotoImage(file="U:\\com404\\2-guis\\5-animation\\3-varying-ticks\\cup1.gif")
        self.cup2_image = PhotoImage(file="U:\\com404\\2-guis\\5-animation\\3-varying-ticks\\cup1 - Copy.gif")
        self.nffc_image = PhotoImage(file="U:\\com404\\2-guis\\5-animation\\3-varying-ticks\\nffc.gif")
        # set window attributes
        self.configure(height=1000,
                       width=1000)

        # set animation attributes
        self.cup1_x_pos = 1
        self.cup1_y_pos = 1
        self.cup1_x_change = 5
        
        self.cup2_x_pos = 1
        self.cup2_y_pos = 200
        self.cup2_x_change = 3

        self.nffc_x_pos = 1
        self.nffc_y_pos = 400
        self.nffc_x_change = 20

        # add components
        self.add_cup1_image_label()
        self.add_cup2_image_label()
        self.add_nffc_image_label()   
        
        # create tick integer
        self.num_ticks = 0
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):

        if (self.num_ticks % 4 == 0):
            if self.cup1_x_pos >= 800 or self.cup1_x_pos <= 0:
                self.cup1_x_change = self.cup1_x_change * -1

            self.cup1_x_pos = self.cup1_x_pos + self.cup1_x_change

            self.cup1_image_label.place(x=self.cup1_x_pos, 
                                    y=self.cup1_y_pos)
        if (self.num_ticks % 10 == 0):
            if self.cup2_x_pos >= 800 or self.cup2_x_pos <= 0:
                self.cup2_x_change = self.cup2_x_change * -1

            self.cup2_x_pos = self.cup2_x_pos + self.cup2_x_change

            self.cup2_image_label.place(x=self.cup2_x_pos, 
                                    y=self.cup2_y_pos)
        if (self.num_ticks % 1 == 0):
            if self.nffc_x_pos >= 800 or self.nffc_x_pos <= 0:
                self.nffc_x_change = self.nffc_x_change * -1

            self.nffc_x_pos = self.nffc_x_pos + self.nffc_x_change

            self.nffc_image_label.place(x=self.nffc_x_pos, 
                                    y=self.nffc_y_pos)

        self.num_ticks += 1
        self.after(100, self.tick)
        
    

    # the ball image
    def add_cup1_image_label(self):
        self.cup1_image_label = Label()
        self.cup1_image_label.place(x=self.cup1_x_pos,
                                    y=self.cup1_y_pos)
        self.cup1_image_label.configure(image=self.cup1_image)

    def add_cup2_image_label(self):
        self.cup2_image_label = Label()
        self.cup2_image_label.place(x=self.cup2_x_pos,
                                    y=self.cup2_y_pos)
        self.cup2_image_label.configure(image=self.cup2_image)

    def add_nffc_image_label(self):
        self.nffc_image_label = Label()
        self.nffc_image_label.place(x=self.nffc_x_pos,
                                    y=self.nffc_y_pos)
        self.nffc_image_label.configure(image=self.nffc_image)

# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop()