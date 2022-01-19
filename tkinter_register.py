from tkinter import *
#import pillow
import ttkwidgets
from ttkwidgets.autocomplete import AutocompleteEntryListbox

import mainprogram  #Module

window=Tk() #instance of frame Tk(),display root window, manages literally everything 

window.geometry('500x500')
window.resizable(width=False, height=False)
window.title('Library Manager')


def printt1():
    print('LibraryManager has been launched')

    global username_login
    global passwd_login
    username_login = fn.get()
    passwd_login = fn2.get()
    
    mainprogram.login()
    #print(first, second)
    return [username_login, passwd_login] #values to pass to login() function

def printt2():
    print('LibraryManager has been launched')

    global username_register
    global passwd_register
    username_register = fn.get()
    passwd_register = fn2.get()
    
    mainprogram.register()
    #print(first, second)
    return [username_register, passwd_register] #values to pass to register() function
    
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
label2 = Label(window, fg='blue', bg='white',text='Access your account', relief='solid',font=('arial',19,)).place(x=80,y=130)

label3 = Label(window, fg='black', text='Username',font=('Arial',12)).place(x=120,y=242)
label3 = Label(window, fg='black' ,text='Password',font=('Arial',12)).place(x=120,y=282)
label1.pack(fill=BOTH)#, pady=2,padx=2
#button1=Button(window, text="Register").place(x=110,y=110)
button1=Button(window, text="Login", relief=GROOVE,command=printt1).place(x=150,y=450)
button1=Button(window, text="Register", relief=GROOVE,command=printt2).place(x=280,y=450)

fn=StringVar()
fn2=StringVar()

entry = Entry(window, textvar=fn).place(x=200,y=242)
entry = Entry(window, show='*',textvar=fn2).place(x=200,y=282)


#droplist
'''var=StringVar()
droplist=OptionMenu(window,var,*l)
var.set('Select book you want to borrow')
droplist.config(width=15)
droplist.place(x=230,y=370)'''
#print(StringVar(),"sv")
#print(type(fn),"fn")
'''
inpute = StringVar()
def auto_complete():
    return inpute.get()
autoc = tkentrycomplete.AutocompleteCombobox(textvariable=inpute)
autoc.set_completion_list(l)
autoc.place(x=110, y=90)'''
