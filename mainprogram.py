'''
login system - username, psswd
Membership code, Book code, Name(book), Author, Issue date, return date, dues
'''

from tkinter import *
from tkinter.ttk import *
import csv
import os
import datetime
#import pillow
#import ttkwidgets

import MainWindow  #modules
import books_issue
import RegistrationPage
import AccountFunctions
#import login #module

def popup(title):
    root = Tk()
    root.title(title)
    label = Label(root, text='Top text').pack()
    root.mainloop()

    
def login():
    global details          #Function called in MainWindow(printt()function)
    details = None
    
    file1 = open('login.txt', 'r+')
    #dic1 = eval(file1.read())   #dic1 needs to be defined

    username = MainWindow.username_login #values passed from printt1()
    passwd = MainWindow.passwd_login 
    l = [username, passwd]
    print(l)
    
    #if l[0] in dic1.keys() and dic1[l[0]] == l[1]:   
     #   print('Login successful')
      #  #verified = True
       # details = [username, passwd]
    #else:
     #   print('Invalid login, try again or EXIT')  #make sure nothing happens
                                                    #checking login, registering users and membership details, lets start with 10 day cap for late fee
    AccountFunctions.open_AccountFunctions()        #To open AccountFunctions Window
    pass


def register():
    global details
    details = None
    file1 = open('login.txt', 'w+')
    #dic1 = eval(file1.read())    #dic1 needs to be defined
    
    #dic1.append([username, passwd])   #file empty so unexpected EOF error, so commented out
    print('Registration successful')

    #verified = True
    #details = [username, passwd]
    #print(details)
    RegistrationPage.open_RegistrationPage()
    # checking login, registering users and membership details
    pass


def issue_book():
    file = open('storage.csv', 'w+')
    w = csv.writer(file, delimiter=',', newline='')
    
    while True:
        l1 = []
#tkinter bs here to select book from dropdown and all that
        issue_date = input("Enter the date of issue (DD/MM/YYYY) - ")
        rn = datetime.datetime.now()
        l1.append(issue_date) #to get when he's issued a book

        #return_date = input("Enter the date of return (DD/MM/YYYY) - ")
        time_change = datetime.delta(days=10)
        duedate = rn + time_change
        l1.append(duedate) #instead of taking input, add 10 to days and display
        print("Book must be returned before", str(duedate)) #HAVE TO PASS TO TKINTER
        #print last return date and threaten late fees TKINTER
        #w.writerow(l1) MAKE CHANGES IN FILE call write() function
        return duedate
    

def storagewrite(duedate):
    file = open('storage.csv', 'w+')

    w = csv.writer(file, delimiter=',', newline='')

    while True:
        l1 = []

        #name_book = input("Enter the name of the book - ")
        #l1.append(name_book) #FETCH BOOK FROM TKINTER dropdown

        issue_date = input("Enter the date of issue (DD/MM/YYYY) - ")
        l1.append(issue_date)
        
        l1.append(duedate)

        w.writerow(l1)


# dont forget newline in output/input |  Membership code, Book code, Name(book), Author, Issue date, return date, dues


def storageread():
    pass


def write():
    with open("Storage.csv", mode="w",) as f1:
        w = csv.writer(f1, delimiter=',', quotechar=" ")
        w.writerow(["Membership Code",  "Book Code", "Book", "Author", "Date of issue", "Date of return", "Fees Due"])
        w.writerow([])
        w.writerow([])
        w.writerow([])
        w.writerow([])

        # GTG CYA


#popup('Bruh')

