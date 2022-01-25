from tkinter import *

import mainprogram
import MainWindow
import AccountFunctions

def open_booksreturn():  #Called function in AccountFunctions.py(Return a book button)
    books_return_window = Toplevel(MainWindow.window)
    books_return_window.geometry('500x500')
    books_return_window.title('Return a book')
    books_return_window.resizable(width=False, height=False)

    frame = Frame(books_return_window, bg = '#DFE7F2')
    frame.pack(expand = True)

    label1 = Label(books_return_window, fg='white', bg='black', text='Return a Book', font=('Arial',24,'bold')).pack(fill=BOTH)

    AccountFunctions.AccountFunctions_window.destroy()
#Need to implement File handling to check if a book needs to be returned, etc.
    
