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

# placing Labels to the main window and using the place() method
label_0 = Label(window, text="Registration Form", width=20, font=("bold", 20),  bg="cyan", fg="black")

#the place method in tkinter is a geometric manager. It is used to organise widgets  by placing them in specific positions
label_0.place(x=90, y=60)

# Label for Fullname and uses the place() method
label_1 = Label(window, text=("Full Name"), width=20, font=("bold", 10), bg="cyan", fg="black")
label_1.place(x=30, y=130)

#Entry: this will accept input strings from the user
entry_1= Entry(window)
entry_1.place(x=200, y=130)

# label for Email 
label_2 = Label(window, text="Email", width=20, font=("bold", 10),  bg="cyan", fg="black")
label_2.place(x=30 ,y=180) 

# Entry for Email
entry_2 = Entry(window)
entry_2.place(x=200, y=180)

# Label for password
label_3 = Label(window, text="Password", width=20, font=("bold", 10), bg="cyan", fg="black")
label_3.place(x=30 ,y=240)

#Entry for password
entry_3= Entry(window, show="*")
entry_3.place(x=200, y=240)

#Label for gender
label_4 = Label(window, text="Gender", width=20, font=("bold", 10), bg="cyan", fg="black")
label_4.place(x=30, y= 290)

Var = IntVar()

# Radiobutton
Radiobutton(window, text="Male", padx=5, variable=Var, value=1).place(x=195, y=290)
Radiobutton(window, text="Female", padx =5, variable=Var ,value=2).place(x=250, y=290)

# Label widget for countries
label_5 = Label(window, text="Country", width=20, font=("bold", 10),  bg="cyan", fg="black")
label_5.place(x=30, y=330)

# list of countries
List_of_countries = ['USA', 'JAPAN', 'CANADA', 'CHINA', 'NIGERIA', 'UK']

c = StringVar()

dropdown = OptionMenu(window,c, *List_of_countries)
dropdown.config(width=15)
c.set("Select your country")
dropdown.place(x=200, y=330)

# label for language
label_6 = Label(window, text="Language", width=20, font=("bold", 10),  bg="cyan", fg="black")
label_6.place(x=30, y=390)

Eng= IntVar()
#check button
Checkbutton(window, text="English", variable=Eng).place(x=185, y=390)

Fre = IntVar()
Checkbutton(window, text="French", variable=Fre).place(x=250, y= 390)

Spa = IntVar()
Checkbutton(window, text="Spanish", variable=Spa).place(x=310, y=390)

# Submit Button
regbutton = Button(window, text="Register", width=20, bg="Blue", fg="white")
regbutton.place(x=180, y= 450)


# This will run the mainloop

window.mainloop()