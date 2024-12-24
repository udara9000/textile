from tkinter import *
from time import strftime

#creating main window
root = Tk()
root.title("clock")

#function to update time 
def time ():
    string = strftime("%I:%M:%S:%p")
    #using %i for 12-hour format
    lbl.config(text = string)
    lbl.after(1000,time)

#creating and atyle the label
lbl = Label(root, 
            font=("calibri",45,"bold"),
            background="fuchsia",foreground="white"
            )
lbl.pack(anchor="center")

#initializing the time update function
time()

#running the main loop...
mainloop()