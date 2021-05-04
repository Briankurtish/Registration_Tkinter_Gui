# Building a Registration Gui application with Tkinter
# Step 1: import Tkinter and all its required Modules

from tkinter import *

# Create a main window (object): Let's call it window

window = Tk()

# Providing Geometry to the Application

window.geometry("500x500")

# Changing the background color of our window
window.config(bg="cyan")

# providing a title to the form
window.title("Registration Form")



# This will run the mainloop

window.mainloop()