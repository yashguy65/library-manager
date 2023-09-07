'''
Takes care of making an account for the user
Adds credentials into login.txt
Opens book issue once registration is over
'''

#Import tkinter, messagebox and os
from tkinter import *
from tkinter import messagebox
import os

#USer defined modules
import mainprogram  
import MainWindow
import books_issue

def open_RegistrationPage():                  #Called function in MainWindow.py(button2)
    global registrationPage_window
    registrationPage_window = Toplevel(MainWindow.window)        #Toplevel used to open new window over MainWindow
    registrationPage_window.geometry('600x600') 
    registrationPage_window.config(bg='light blue')
    registrationPage_window.title('Registration Page')
    registrationPage_window.resizable(width=False, height=False)
    MainWindow.window.withdraw()

    #Titles
    label1 = Label(registrationPage_window, fg='white', bg='black', text='Make Your Account', font=('Arial',24,'bold')).pack(fill=BOTH)
    label2 = Label(registrationPage_window, fg='white', bg='black', text='Account Details:', font=('Arial',15)).place(x=20, y=60)

    #Area to enter acc details
    #Name Entry
    name_label = Label(registrationPage_window, fg='black', bg='white', text='Name:', font=('Arial', 12)).place(x=40, y=110)
    global name_register_init
    name_register_init = StringVar()
    name_entry = Entry(registrationPage_window, textvar=name_register_init).place(x=150,y=110)

    #Age entry
    age_label = Label(registrationPage_window, fg='black', bg='white', text='Age:', font=('Arial', 12)).place(x=40, y=160)
    global age_register_init
    age_register_init = IntVar()
    age_entry = Entry(registrationPage_window, textvar=age_register_init).place(x=150,y=160)

    #Phone number entry
    ph_number_label = Label(registrationPage_window, fg='black', bg='white', text='Phone Number:', font=('Arial', 12)).place(x=40, y=210)
    global ph_number_register_init
    ph_number_register_init = IntVar()
    ph_number_entry = Entry(registrationPage_window, textvar=ph_number_register_init).place(x=180,y=210)

    #Username Entry
    username_register_label = Label(registrationPage_window, fg='black', bg='white', text='Enter Username:', font=('Arial', 12)).place(x=40, y=260)
    global username_register_init
    username_register_init = StringVar()
    username_register_entry = Entry(registrationPage_window, textvar=username_register_init).place(x=180,y=260)

    #Password Entry
    password_register_label = Label(registrationPage_window, fg='black', bg='white', text='Enter Password:', font=('Arial', 12)).place(x=40, y=310)
    global password_register_init
    password_register_init = StringVar()
    password_register_entry = Entry(registrationPage_window, show='*', textvar=password_register_init).place(x=180, y=310)
    
    #Dropdown of payment methods
    pay_method = Label(registrationPage_window, fg='white', bg='black', text='Payment Method:', font=('Arial', 15)).place(x=20, y=390)
    list_methods = ['Cash','Debit Card','Cashapp','Paytm','PhonePe','Google Pay','Samsung Pay', 'Venmo']
    global variable
    variable = StringVar()
    dropdown = OptionMenu(registrationPage_window, variable, *list_methods)
    dropdown.config(width=20)
    dropdown.place(x=300, y=390)

    confirm_button = Button(registrationPage_window, text='Confirm', relief=GROOVE, command=ObtainRegistrationValues).place(x=60, y=450)

username_register = ''
#Obtaining all entered values
def ObtainRegistrationValues():

    #Called function in RegistrationPage.py confirm button
    name_register = name_register_init.get()
    age_register = age_register_init.get()
    ph_number_register = ph_number_register_init.get()
    global username_register
    username_register = username_register_init.get()
    password_register = password_register_init.get()
    choice_method = variable.get()

    
    tup = [name_register, age_register, ph_number_register, username_register, password_register, choice_method]   #list of entered values
    print(name_register, age_register, ph_number_register, username_register, password_register, choice_method)

    booly = True
    if os.path.exists('login.txt'):
        file1 = open('login.txt', 'r+')     #checking if login.txt exists
        dic1 = eval(file1.read())
        l = [tup[3], tup[4]]
        l = list(l)               #Getting username, password from tup
        print('dic1', dic1, type(dic1))
        
        if len(dic1) != 0:
            userlist = []
            for k in range(len(dic1)):
                userlist.append(dic1[k][0])    #Appending username to userlist
            print('userlist', userlist)
            
            if l[0] in userlist:               #Checking if username already exists
                popup('Username Taken')
                booly = False
            else:
                dic1.append(l)           #appending list to dic1
                file1.seek(0)
                
                
                file1.write(listToString(dic1))             #converting list dic1 to string
                file1.close()                               #writing into file1
            
        else:
            l2 = [l]
            file1.seek(0)
            file1.write(listToString(l2))      #If dic1 empty
            file1.close()
    else:
        file1 = open('login.txt', 'w+')         #if login.txt doesn't exist       
        l = [tup[3], tup[4]]
        l2 = [l]
        file1.write(listToString(l2))           
        file1.close()

    if booly:
        registrationPage_window.destroy()     #destroying registration page
        books_issue.open_booksissue()       #opening books_issue if username is valid

    else:
        pass                        
    
def listToString(s):
    str1 = "" 

    for ele in s: 
        str1 += str(ele)                  #function to convert list to string
        
    str2 = str1.replace('][', '],[')
    str3 = '[' + str2 + ']'  
    return str3
