from tkinter import *
from tkinter import messagebox
import os

import mainprogram  #modules
import MainWindow
import books_issue

def open_RegistrationPage():   #Called function in MainWindow.py(button2)
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
    #exit_button = Button(registrationPage_window, text='Back to Main Window', relief=GROOVE, command=exit_RegistrationPage).place(x=60, y=480)

#Obtaining all entered values
def ObtainRegistrationValues():

    #Called function in RegistrationPage.py confirm button
    name_register = name_register_init.get()
    age_register = age_register_init.get()
    ph_number_register = ph_number_register_init.get()
    username_register = username_register_init.get()
    password_register = password_register_init.get()
    choice_method = variable.get()

    
    tup = [name_register, age_register, ph_number_register, username_register, password_register, choice_method]
    print(name_register, age_register, ph_number_register, username_register, password_register, choice_method)

    booly = True
    if os.path.exists('login.txt'):
        file1 = open('login.txt', 'r+')
        dic1 = list((file1.read().strip(', ')))
        l = [tup[3], tup[4]]
        l = list(l)
        if len(dic1) != 0:
            userlist = []
            for k in range(len(dic1)):
                userlist.append(dic1[k][0])
            
            if l[0] in userlist:
                popup('Username Taken')
                booly = False
            else:
                dic1.append(l)
                file1.seek(0)
                
                
                file1.write(listToString(dic1))    
                file1.close()
            
        else:
            l2 = [l]
            file1.seek(0)
            file1.write(listToString(l2))      #str(l2)
            file1.close()
    else:
        file1 = open('login.txt', 'w+')
        l = [tup[3], tup[4]]
        l2 = [l]
        
        
        file1.write(listToString(l2))            #str(l2)
        file1.close()

    if booly:
        registrationPage_window.destroy()
        books_issue.open_booksissue()

    else:
        pass


    
    #checking login, registering users and membership details
    #messagebox.showinfo('Account Created!', 'Go back to the Main Window and login again!')
    
    
'''
#Closing registration page, reopening MainWindow ez
def exit_RegistrationPage():
    registrationPage_window.destroy()
    MainWindow.window.deiconify()
'''
def listToString(s):
    str1 = "" 

   
    for ele in s: 
        str1 += str(ele)

    return str1

    
'''
file1 = open('login.txt', 'a+')
    dic1 = [file1.read()]
    print(dic1)
    l = [tup[3], tup[4]]
    dic1.append(l)
    file1.write(str(l))
    file1.close()
    print('Registration successful')
'''
