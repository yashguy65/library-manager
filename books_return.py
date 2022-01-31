from tkinter import *
from datetime import date
import mainprogram
import MainWindow
import AccountFunctions

def open_booksreturn(username,bookname,duedate):  #Called function in AccountFunctions.py(Return a book button)
    books_return_window = Toplevel(MainWindow.window)
    books_return_window.geometry('500x500')
    books_return_window.title('Return a book')
    books_return_window.resizable(width=False, height=False)

    frame = Frame(books_return_window, bg = '#DFE7F2')
    frame.pack(expand = True)
    rn = date.today
    delta = duedate - rn
    days = delta.days
    if delta.days<10:
        latefee = 0
    else:
        latefee = 50

    label1 = Label(books_return_window, fg='white', bg='black', text='Return a Book', font=('Arial',24,'bold')).pack(fill=BOTH)
    #label2 = Label(books_return_window, fg='white', bg='black', text=f'{username}', font=('Arial',24,'bold')).pack(fill=BOTH)
    label3 = Label(books_return_window, fg='white', bg='black', text=f'Book Title: {bookname}', font=('Arial',24,'bold')).pack(fill=BOTH)
    label4 = Label(books_return_window, fg='white', bg='black', text=f'Due Date: {duedate}', font=('Arial',24,'bold')).pack(fill=BOTH)
    label5 = Label(books_return_window, fg='white', bg='black', text=f'You have to pay {latefee} as late fees', font=('Arial',24,'bold')).pack(fill=BOTH)

    def switch_state():
        if pay['state'] == NORMAL:
            pay['state'] = DISABLED

    if latefee != 0:
        #display pay now button
        pay = Checkbutton(text="Pay now", state=NORMAL,command=switch_state)
        pay.pack(side=BOTTOM)

    AccountFunctions.AccountFunctions_window.destroy()

    
