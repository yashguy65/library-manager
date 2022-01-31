from tkinter import *
from tkinter.ttk import *
import csv

# csv for login details

mainscreen = Tk()   # create a GUI window
mainscreen.geometry("800x800")  # set the configuration of GUI window
mainscreen.title(" Login Page")  # set the title of GUI window
# create a Form label
Label(label="Login Window Example", bg="blue",width="30", height="2", font=("Calibri", 13)).pack()
Label(label="").pack()
# create Login Button
Button(label="Login", height="2", width="30").pack()
Label(label="").pack()
# create a register button
Button(label="Register", height="2", width="30").pack()
