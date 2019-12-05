from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.red_ball_image = PhotoImage(file="U:\com404\\2-guis\\5-animation\\2-multiple-components\\redball.gif")
        self.blue_ball_image = PhotoImage(file="U:\com404\\2-guis\\5-animation\\2-multiple-components\\blueball.gif")
        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.red_ball_x_pos = 150
        self.red_ball_y_pos = 1
        self.red_ball_x_change = 5
        self.red_ball_y_change = 5

        self.blue_ball_x_pos = 1
        self.blue_ball_y_pos = 150
        self.blue_ball_x_change = 5
        self.blue_ball_y_change = 5

     # add components
        self.add_red_ball_image_label() 
        self.add_blue_ball_image_label()
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        if self.red_ball_x_pos >= 275 or self.red_ball_x_pos <= 0:
            self.red_ball_x_change = self.red_ball_x_change * -1

        if self.red_ball_y_pos >= 275 or self.red_ball_y_pos <= 0:
            self.red_ball_y_change = self.red_ball_y_change * -1

        self.red_ball_x_pos = self.red_ball_x_pos + self.red_ball_x_change
        self.red_ball_y_pos = self.red_ball_y_pos + self.red_ball_y_change
        self.red_ball_image_label.place(x=self.red_ball_x_pos, 
                                y=self.red_ball_y_pos)

# BLUE BALL
        if self.blue_ball_x_pos >= 275 or self.blue_ball_x_pos <= 0:
            self.blue_ball_x_change = self.blue_ball_x_change * -1
            
        if self.blue_ball_y_pos >= 275 or self.blue_ball_y_pos <= 0:
            self.blue_ball_y_change = self.blue_ball_y_change * -1

        self.blue_ball_x_pos = self.blue_ball_x_pos + self.blue_ball_x_change
        self.blue_ball_y_pos = self.blue_ball_y_pos + self.blue_ball_y_change

        self.blue_ball_image_label.place(x=self.blue_ball_x_pos, 
                                y=self.blue_ball_y_pos)


        self.after(100, self.tick)    
    

    # the ball image
    def add_red_ball_image_label(self):
        self.red_ball_image_label = Label()
        self.red_ball_image_label.place(x=self.red_ball_x_pos,
                                    y=self.red_ball_y_pos)
        self.red_ball_image_label.configure(image=self.red_ball_image)
    
    def add_blue_ball_image_label(self):
        self.blue_ball_image_label = Label()
        self.blue_ball_image_label.place(x=self.blue_ball_x_pos,
                                    y=self.blue_ball_y_pos)
        self.blue_ball_image_label.configure(image=self.blue_ball_image)
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop()