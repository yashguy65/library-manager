'''
#Module for asking the user what to do after logging in

#Importing tkinter
from tkinter import *

import mainprogram  #Modules
import MainWindow
import books_issue
import books_return

def open_AccountFunctions():        #Called function in mainprogram.py(login())
    global AccountFunctions_window
    AccountFunctions_window = Toplevel(MainWindow.window)
    AccountFunctions_window.geometry('300x200')                           #Add another option to change account details if time permits?
    AccountFunctions_window.title('Welcome To Library Manager')
    AccountFunctions_window.resizable(width=False, height=False)

    label1 = Label(AccountFunctions_window, fg='white', bg='black', text='What would you like to do?', font=('Arial',15,'bold')).pack(fill=BOTH)

    issue_button = Button(AccountFunctions_window, text='Issue a book', relief=GROOVE, command=books_issue.open_booksissue).place(x=100, y=70)
    return_button = Button(AccountFunctions_window, text = 'Return a book', relief=GROOVE, command=books_return.open_booksreturn).place(x=100, y=130)
'''


