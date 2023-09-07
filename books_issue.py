'''
The book issue window
Has a list of over 100 books to display to the user
Has Autocomplete Entry
Obtains issued book and writes it into storage.csv with required user credentials
'''

#Importing Tkinter
from tkinter import *

from tkinter import ttk
import ttkwidgets
from ttkwidgets.autocomplete import AutocompleteEntry     #Importing all needed modules and widgets
import datetime
import csv

#Modules
import mainprogram
import MainWindow
import RegistrationPage

def popup(title, text, text1, text2):
    global root
    root = Tk()
    root.title(title)                              #Function to create a popup
    root.geometry('350x420')
    root.config(bg='light blue') 
    label = Label(root, fg='white', bg='black', text=text, font=('Arial',12)).pack()
    label1 = Label(root, fg='white', bg='black', text = text1, font=('Arial',12)).pack()
    label1 = Label(root, fg='white', bg='black', text = text2, font=('Arial',12)).pack()
    button1 = Button(root, text = 'Back To Main Window', command = exitt).pack(side=BOTTOM)
    
    root.mainloop()

def exitt():
    root.destroy()
    books_issue_window.destroy()                            #Exit Book issue window
    MainWindow.window.deiconify()  #Brings MainWindow back
    
def open_booksissue():
    #Called function in mainprogram.py
    global books_issue_window
    books_issue_window = Toplevel(MainWindow.window)  #To open new window when login clicked
    books_issue_window.geometry('500x500')
    books_issue_window.title('Issue a book')
    books_issue_window.config(bg='light blue')
    books_issue_window.resizable(width=False, height=False)
    MainWindow.window.withdraw()

    frame = Frame(books_issue_window)   #Creates a frame for the listbox
    frame.place(x=40, y=200)

    #Titles
    label1 = Label(books_issue_window, fg='white', bg='black', text='Issue a Book', font=('Arial',24,'bold')).pack(fill=BOTH)
    label2 = Label(books_issue_window, fg='white', bg='black', text='Book List:', font=('Arial',15)).place(x=20, y=60)

    global getBookbutton
    getBookbutton = Button(books_issue_window, text = 'Issue', state = NORMAL, command = getbook)
    getBookbutton.pack(side=BOTTOM)
    
    list_books=['The Daughter of Time','The Big Sleep','The Spy Who Came In From the Cold','Gaudy Night','The Murder of Roger Ackroyd','Rebecca',
       'Farewell My Lovely','The Moonstone','The IPCRESS File','The Maltese Falcon','The Franchise Affair','Last Seen Wearing ...',
       'The Name of the Rose','Rogue Male','The Long Goodbye','Malice Aforethought','The Day of the Jackal','The Nine Tailors',
       'And Then There Were None','The Thirty-Nine Steps','The Collection: Sherlock Holmes','Murder Must Advertise',
       'Tales of Mystery & Imagination','The Mask of Dimitrios','The Moving Toyshop','The Tiger in the Smoke',        #All list of books
       'The False Inspector Dew','The Woman in White','A Dark-Adapted Eye','The Postman Always Rings Twice','The Glass Key',
       'The Hound of the Baskervilles','Tinker, Tailor, Soldier, Spy',"Trent's Last Case",'From Russia, with Love','Cop Hater',
       'The Dead of Jericho','Strangers on a Train','A Judgement in Stone','The Hollow Man',
       'The Poisoned Chocolates Case','A Morbid Taste for Bones','The Leper of Saint Giles','A Kiss Before Dying','The Talented Mr. Ripley', #Get Indian books
       'Brighton Rock','The Lady in the Lake','Presumed Innocent','A Demon in My View','The Devil in Velvet','A Fatal Inversion',
       'The Journeying Boy','A Taste for Death','The Eagle Has Landed','My Brother Michael',
       'Bertie and the Tin Man','Penny Black','Game, Set & Match','The Danger','Devices and Desires',
       'Under World','Nine Coaches Waiting','A Running Duck','Smallbone Deceased','The Rose of Tibet','Innocent Blood',
       'Strong Poison','Hamlet, Revenge!','A Thief of Time','A Bullet in the Ballet','Deadheads','The Third Man','The Labyrinth Makers',
       'The Berlin Memorandum','Beast in View','The Shortest Way to Hades','Running Blind','Twice Shy',
       'The Manchurian Candidate',"Killings at Badger's Drift",'The Beast Must Die','Gorky Park',
       'Death Comes as the End','Green for Danger','Tragedy at Law','The Collector',"Gideon's Day",
       'The Sun Chemist','The Guns of Navarone','The Colour of Murder','Greenmantle','The Riddle of the Sands','Wobble to Death',
       'Red Harvest','The Key to Rebecca','Sadie When She Died','The Murder of the Maharajah','What Bloody Man Is That?','Shooting Script',
       'The Four Just Men']

    global book_var
    book_var = StringVar(books_issue_window)
    
    entry1 = AutocompleteEntry(
        books_issue_window,                       #Creates listbox
        width = 50,
        textvariable = book_var,
        font = ('Arial', 18),
        completevalues = list_books
        ).pack(padx = 40, pady = 120)

    allbooks_var = StringVar(value=list_books)
    listbox = Listbox(
        frame,
        listvariable=allbooks_var,
        width = 50,
        height = 10,
        )
    listbox.pack(side='left', fill='y')

    scrollbar = Scrollbar(
        frame,
        orient = 'vertical',
        command=listbox.yview
        )
    scrollbar.pack(side='right', fill='y')

    listbox.config(yscrollcommand=scrollbar.set)


def storagewrite(username, book ,duedate):
    file1 = open('storage.csv', 'a+', newline = '')         #Function to write issue details into storage
    w = csv.writer(file1, delimiter=',')
    w.writerow([username,book,duedate])
    file1.close()
    
def getbook():
    issued_book = book_var.get()
    print(issued_book)
    mainprogram.switch_state(getBookbutton)                 #Function to get all book details

    rn = datetime.date.today()
    duedate = rn + datetime.timedelta(days=10)
    bookname = str(issued_book)

    if str(RegistrationPage.username_register) == '':
        namey = mainprogram.lol[0]
    else:
        namey = RegistrationPage.username_register
        
    storagewrite(str(namey),bookname, duedate)
    popup("Confirmation", "Your Book has been issued", str(duedate), bookname) #print last return date and threaten late fees 
    



