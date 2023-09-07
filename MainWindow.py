'''
The MainWindow of Project LIBMAN (Code 007)
Has areas to enter username and password
Passes value to mainprogram
'''

#Import tkinter
from tkinter import *
import ttkwidgets

#User defined modules
import mainprogram  

#Main Window instance
window=Tk() 
window.geometry('500x500')
window.config(bg='light blue')
window.resizable(width=False, height=False)
window.title('Library Manager')

#labels
label1 = Label(window, fg='white', bg='black',text='Welcome to Library manager', font=('Arial',20,'bold'))
label2 = Label(window, fg='white', bg='black',text='Access your account', relief='solid',font=('arial',19,)).place(x=120,y=80)

label3 = Label(window, fg='black', bg='white', text='Username',font=('Arial',12)).place(x=120,y=170)
label3 = Label(window, fg='black', bg='white', text='Password',font=('Arial',12)).place(x=120,y=232)
label4 = Label(window, fg='black', bg='white', text="Don't have an account? Make one here:", font=('Arial',12)).place(x=200,y=415)
label1.pack(fill=BOTH)

#Gets username, password entered by user
def printt():
    print('LibraryManager has been launched')

    global username_login
    global passwd_login
    username_login = fn.get()
    passwd_login = fn2.get()
    return [username_login, passwd_login] 

#Buttons
button1=Button(window, text="Login", relief=GROOVE,command=mainprogram.login).place(x=210,y=320)
button1=Button(window, text="Register", relief=GROOVE,command=mainprogram.register).place(x=400,y=450)

fn=StringVar()
fn2=StringVar()

entry = Entry(window, textvar=fn).place(x=200,y=170)               #Username, psswd stored in fn and fn2
entry = Entry(window, show='*',textvar=fn2).place(x=200,y=232)


def invalid_login():
    label3 = Label(window, fg='black', text='Account does not exist', font=('Arial',12)).place(x=60,y=250)   #message for invalid login

def exitt():  #To exit
    exit()
