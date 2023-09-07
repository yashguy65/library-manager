'''
Project LIBMAN (Code 007)
Library Manager
'''

'''
Main module for centralized flow of execution
Main functions called here
'''

#Importing Modules
import csv
from tkinter import *
import csv
import time
import ttkwidgets
import os

#User defined modules
import MainWindow  
import books_issue
import books_return
import RegistrationPage

#Create popup
def popup(title, text):
    root = Tk()
    root.title(title)
    label = Label(root, text=text).pack()
    root.mainloop()


def login():
    global details                            #Function called in MainWindow(printt()function)
    details = ['username','password']
    if not os.path.exists('storage.csv'):      #Checking if file exists or not
        file1 = open('storage.csv', 'w')
        file1.close()
        
    if os.path.exists('login.txt'):
        file1 = open('login.txt', 'r+')
        dic2 = file1.read()                 #dic2 with all usernames and passwords
        
        res = eval(dic2)                    #using eval to get nested list of usernames and passwords
        global dic1
        dic1 = res.copy()
                
        global lol
        lol = MainWindow.printt()
        
        details = [lol[0], lol[1]]
        
        username_list = []
        for k in range(len(dic1)):             #Creating list of usernames
            username_list.append(dic1[k][0])
            
        if details[0] in username_list:
            for k in range(len(dic1)):
                if dic1[k][0] == details[0]:
                    if dic1[k][1] == details[1]:       #Checking login credentials
                        print('Login successful')
                        file1 = open('storage.csv','r+', newline='')
                        reader = csv.reader(file1, delimiter=',')
                        listy=[]
                        
                        for row in reader:
                            if row != []:
                                listy.append(row[0])
                        print('listy', listy)
                        
                        if lol[0] in listy:         #Checking if book issued or not
                            return_book()           #Opening book_issue or book_return based on issue status
                        else:
                            issue_book()

        else:
            popup('Username Not Found', 'Username Not Found')      #Displaying message if no account exists

        file1.close()
    else:
        register()             
        
    
def register():              #Register
    RegistrationPage.open_RegistrationPage()


def issue_book():     #book issue
    books_issue.open_booksissue()

    
def return_book():    #return book
    file1 = open('storage.csv','r+')
    reader = csv.reader(file1, delimiter=',')
    listy=[]
    for row in reader:                        
        if row != []:
            if row[0] == details[0]:                    #passing values to function in books_return
                listy = list(row)
    print('listy2', listy[2], type(listy[2]))
    books_return.open_booksreturn(listy[0],listy[1],listy[2])
    file1.close()
    pass


def switch_state(button):
    if button['state'] == NORMAL:             #Disables button once pressed
        button['state'] = DISABLED
        returned = True
