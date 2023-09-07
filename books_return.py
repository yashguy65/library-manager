'''
The books return window
Calculates the number of days the book has been issued
Checks if late fee needs to be paid
Erases returned book from storage.csv
'''

#Importing Tkinter
from tkinter import *
import datetime

#Importing required modules
import os
import csv

#User Defined Modules
import mainprogram
import MainWindow

returned=False

#Function to open book return
def open_booksreturn(username,bookname,duedate2):  #Called function in mainprogram.py
    global books_return_window
    books_return_window = Toplevel(MainWindow.window)
    books_return_window.geometry('500x500')
    books_return_window.title('Return a book')
    books_return_window.config(bg='light blue')
    books_return_window.resizable(width=False, height=False)
    duedate3 = datetime.datetime.strptime(duedate2, '%Y-%m-%d')
    duedate = duedate3.date()
    
    frame = Frame(books_return_window, bg = '#DFE7F2')
    frame.pack(expand = True)
    rn = datetime.date.today()               #Gets current day
    delta = duedate - rn                     #Calculating due date
    
    print((10-int(delta.days)), 'days since book was issued')
    if delta.days>0:
        latefee = 0                       #Checking if late fee needs to be given
    else:
        latefee = 50

    #Labels
    label1 = Label(books_return_window, fg='white', bg='black', text='Return a Book', font=('Arial',20,'bold')).pack(fill=BOTH)
    label3 = Label(books_return_window, fg='white', bg='black', text=f'Book Title: {bookname}', font=('Arial',15,'bold')).pack(fill=BOTH)
    label4 = Label(books_return_window, fg='white', bg='black', text=f'Due Date: {duedate}', font=('Arial',20,'bold')).pack(fill=BOTH)
    label5 = Label(books_return_window, fg='white', bg='black', text=f'You have to pay {latefee} as late fees', font=('Arial',20,'bold')).pack(fill=BOTH)

    def switch_state():
        global returned
        if returned == False:
            file = open('storage.csv', 'r+', newline = '')           #Function to remove issue details from when book returned
            file2 = open('temp.csv','w')
            writer = csv.writer(file2, delimiter=',')
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row != []:
                    if row[0] != username:
                        writer.writerow(row)
            file.close()
            file2.close()
            os.remove('storage.csv')
            os.rename('temp.csv','storage.csv')

            file.close()

        
        if pay['state'] == NORMAL:         #Disabling the return button
            pay['state'] = DISABLED
            returned=True
        books_return_window.destroy()   #Destroying book retrun window

    if latefee != 0:
        #display pay now button
        pay = Button(books_return_window, text="Pay now", state=NORMAL,command=switch_state)   #Payment
        pay.pack()

    if latefee == 0:
        #display pay now button
        pay = Button(books_return_window, text="Return", state=NORMAL,command=switch_state)
        pay.pack()

    

    
