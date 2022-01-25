from tkinter import *
#import pillow
import ttkwidgets
from ttkwidgets.autocomplete import AutocompleteEntryListbox

import mainprogram  #Modules
import books_issue
import RegistrationPage

window=Tk() #instance of frame Tk(),display root window, manages literally everything 

window.geometry('500x500')
window.resizable(width=False, height=False)
window.title('Library Manager')


def printt():
    print('LibraryManager has been launched')

    global username_login
    global passwd_login
    username_login = fn.get()
    passwd_login = fn2.get()
    
    mainprogram.login()   #Add verification of username, psswd
                          #Make sure username, psswd columns not empty
                          #Add username, psswd to file(appending function in mainprogram.py)
    
    #print(first, second)
    return [username_login, passwd_login] #values to pass to login() function

'''
def printt2():
    print('LibraryManager has been launched')

    #global username_register
    #global passwd_register                       #printt2() not being used after getting RegistrationPage.py
    #username_register = fn.get()
    #passwd_register = fn2.get()
    
    #mainprogram.register()    
    #print(first, second)
    return [username_register, passwd_register] #values to pass to register() function
'''
    
def exitt():
    exit()

#path=r'C:\Users\yoyas\3D Objects\logo.png'   
#photo1=PhotoImage(file=path)
#photo = photo1.subsample(5, 5)
#lab = Label(image=photo)
#lab.place(x=130,y=130)

#larger_image = image.zoom(2, 2)         #create a new image twice as large as the original
#smaller_image = image.subsample(2, 2)   #create a new image half as large as the original

label1 = Label(window, fg='blue', bg='white',text='Welcome to Library manager', font=('Arial',20,'bold'))
label2 = Label(window, fg='blue', bg='white',text='Access your account', relief='solid',font=('arial',19,)).place(x=120,y=80)

label3 = Label(window, fg='black', text='Username',font=('Arial',12)).place(x=120,y=170)
label3 = Label(window, fg='black' ,text='Password',font=('Arial',12)).place(x=120,y=232)
label4 = Label(window, fg='black', text="Don't have an account? Make one here:", font=('Arial',12)).place(x=200,y=415)
label1.pack(fill=BOTH)#, pady=2,padx=2

button1=Button(window, text="Login", relief=GROOVE,command=printt).place(x=210,y=320)
button1=Button(window, text="Register", relief=GROOVE,command=RegistrationPage.open_RegistrationPage).place(x=400,y=450)

fn=StringVar()
fn2=StringVar()

entry = Entry(window, textvar=fn).place(x=200,y=170)               #Username, psswd stored in fn and fn2
entry = Entry(window, show='*',textvar=fn2).place(x=200,y=232)
