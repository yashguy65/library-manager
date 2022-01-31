'''
login system - username, psswd
Membership code, Book code, Name(book), Author, Issue date, return date, dues
'''
import csv
from tkinter import *
from tkinter.ttk import *
import csv
from datetime import date, timedelta
#import pillow
#import ttkwidgets

import MainWindow  #modules
import books_issue
import books_return
import RegistrationPage
import AccountFunctions

def popup(title):
    root = Tk()
    root.title(title)
    label = Label(root, text='Top text').pack()
    root.mainloop()

    
def login():
    global details          #Function called in MainWindow(printt()function)
    details = None
    AccountFunctions.open_AccountFunctions() 
    file1 = open('login.txt', 'r+')
    dic1 = eval(file1.read())   
    dic1 = list(dic1)
    username, passwd = MainWindow.printt()
    #username = MainWindow.username_login #values passed from printt()
    #passwd = MainWindow.passwd_login 
    l = [username, passwd]
    print(l)
    
    if l[0] in dic1.keys() and dic1[l[0]] == l[1]:   
        print('Login successful')
        details=l.copy()
    #check if pending book to be returned
    file1 = open('storage.csv','w+')
    reader = csv.reader(file1, delimiter=',', newline='')
    listy=[]
    for row in reader:
        if row[1] != '':
            listy.append(row[0])
    if details[0] in listy:
        return_book()
    else:
        issue_book()


    #else:
    #   print('Invalid login, try again or EXIT')  #make sure nothing happens
                                                    #checking login, registering users and membership details, lets start with 10 day cap for late fee
        #To open AccountFunctions Window
    


def register():
    RegistrationPage.open_RegistrationPage()
    file1 = open('login.txt', 'w+')
    dic1 = eval(file1.read())   
    dic1 = list(dic1) 
    tup = RegistrationPage.ObtainRegistrationValues()
    l = [tup[3], tup[4]]
    dic1.append(l)
    file1.write(l)
    file1.close()
    print('Registration successful')
    # checking login, registering users and membership details
    


def issue_book():
    books_issue.open_booksissue()
#tkinter bs here to select book from dropdown and all that
    rn = date.today()
    duedate = rn + timedelta(days=10)
    print("Book must be returned before", str(duedate)) #print last return date and threaten late fees TKINTER
    bookname = 'return in issue book function'
    storagewrite(details[0],bookname,duedate)
    
def return_book():
    file1 = open('storage.csv','w+')
    reader = csv.reader(file1, delimiter=',', newline='')
    listy=[]
    for row in reader:
        if row[0] == details[0]:
            listy = list(row)    
    books_return.open_booksreturn(listy[0],listy[1],listy[2])
    pass


def storagewrite(username, book ,duedate):
    file = open('storage.csv', 'w+')
    #COLUMNS:- USERNAME | BOOK ISSUED | DUE DATE | 
    w = csv.writer(file, delimiter=',', newline='')
    w.writerow([username,book,duedate])
    file.close()

# dont forget newline in output/input 
#event loops

#popup('Bruh')

