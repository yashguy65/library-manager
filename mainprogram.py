'''
login system - username, psswd
Membership code, Book code, Name(book), Author, Issue date, return date, dues
'''

from tkinter import *
from tkinter.ttk import *
import csv


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
    dic1.append([username, passwd])
    print('Registration successful')
    verified = True
    details = [username, passwd]
    # checking login, registering users and membership details
    pass


def login():
    global details
    details = None
    file1 = open('login.txt', 'r+')
    dic1 = eval(file1.read())
    username = input('Enter username: ')
    paswd = input('Enter password: ')
    l = [username, passwd]
    if l in dic1:
        print('Login successful')
        verified = True
        details = [username, passwd]
    else:
        print('Invalid login, try again or EXIT')
    # checking login, registering users and membership details
    pass


def storagewrite():
    file = open('storage.csv', 'w+')

    w = csv.writer(file, delimiter=',', newline='')

    while True:
        l1 = []
        membership_code = input("Enter the membership code - ")
        l1.append(membership_code)

        book_code = input("Enter the book code - ")
        l1.append(book_code)

        name_book = input("Enter the name of the book - ")
        l1.append(name_book)

        name_author = input("Enter the name of the author - ")
        l1.append(name_author)

        issue_date = input("Enter the date of issue (DD/MM/YYYY) - ")
        l1.append(issue_date)

        return_date = input("Enter the date of return (DD/MM/YYYY) - ")
        l1.append(return_date)

        w.writerow(l1)


# dont forget newline in output/input |  Membership code, Book code, Name(book), Author, Issue date, return date, dues
    pass


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
