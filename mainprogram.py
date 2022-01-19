'''
login system - username, psswd
Membership code, Book code, Name(book), Author, Issue date, return date, dues
'''

from tkinter import *
from tkinter.ttk import *
import csv
import os
import datetime
import tkinter_register #module
import login #module


def popup(title):
    root = Tk()
    root.title(title)
    label = Label(root, text='Top text').pack()
    root.mainloop()

    
def register():
    global details
    details = None
    file1 = open('login.txt', 'w+')
    dic1 = eval(file1.read())
    username = input('Enter new username: ')
    passwd = input('Enter new password: ')
    dic1.append([username, passwd]) #work in tkinter
    print('Registration successful')
    #verified = True
    details = [username, passwd]
    # checking login, registering users and membership details
    pass


def login():
    global details
    details = None
    file1 = open('login.txt', 'r+')
    dic1 = eval(file1.read())
    username = input('Enter username: ')
    paswd = input('Enter password: ') #take in from tkinter
    l = [username, passwd]
    if l[0] in dic1.keys() and dic1[l[0]] == l[1]:
        print('Login successful')
        #verified = True
        details = [username, passwd]
    else:
        print('Invalid login, try again or EXIT') #make sure nothing happens
    # checking login, registering users and membership details, lets start with 10 day cap for late fee
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
        duedate= t=rn + time_change
        l1.append(duedate) #instead of taking input, add 10 to days and display
        print("Book must be returned before", str(duedate)) #HAVE TO PASS TO TKINTER
        #print last return date and threaten late fees TKINTER
        #w.writerow(l1) MAKE CHANGES IN FILE call write() function


def storagewrite():
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
        w.writerow(["Membership Code",  "Book Code", "Book",
                   "Author", "Date of issue", "Date of return", "Fees Due"])
        w.writerow([])
        w.writerow([])
        w.writerow([])
        w.writerow([])

        # GTG CYA


popup('Bruh')
