from tkinter import *
window=Tk() #instance of tkinter frame, i.e., Tk() It helps to display the root window and manages all the other components of the tkinter application. We can initialize the tkinter instance by assigning the variable to it.

window.geometry('500x500')
window.title('Library Manager')

def printt():
    print('LibraryManager has been launched')
    first=fn.get()
    

def exitt():
    exit()

path=r'C:\Users\yoyas\3D Objects\logo.png'
photo1=PhotoImage(file=path)
photo = photo1.subsample(2, 2)
lab = Label(image=photo)
lab.place(x=130,y=130)

#larger_image = image.zoom(2, 2)         #create a new image twice as large as the original
#smaller_image = image.subsample(2, 2)   #create a new image half as large as the original

label1 = Label(window, fg='blue', bg='white',text='Welcome to Library manager', font=('Arial',20,'bold'))
label2 = Label(window, fg='blue', bg='white',text='Access your account', relief='solid',font=('arial',19,)).place(x=80,y=130)
label1.pack(fill=BOTH)#, pady=2,padx=2)
#button1=Button(window, text="Register").place(x=110,y=110)
button1=Button(window, text="Register", relief=GROOVE,command=printt).place(x=250,y=250)

fn=StringVar()
entry = Entry(window, textvar=fn).place(x=240,y=242)
l=['lol','rofl','lmao','lulw','xd']
var=StringVar()
droplist=OptionMenu(window,var,*l)
var.set('select fav v of laugh')
droplist.config(width=15)
droplist.place(x=230,y=370)
#print(StringVar(),"sv")
#print(type(fn),"fn")

