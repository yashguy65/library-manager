'''
login system - username, psswd
Membership code, Book code, Name(book), Author, Issue date, return date, dues
'''

import csv
from tkinter import *
import csv
#from datetime import date, timedelta
import time
#import pillow
import ttkwidgets

import MainWindow  #modules
import books_issue
import books_return
import RegistrationPage


def popup(title, text):
    root = Tk()
    root.title(title)
    label = Label(root, text=text).pack()
    root.mainloop()

   
def login():
    global details      #Function called in MainWindow(printt()function)
    details = ['username','password']
    #if __name__ == "__main__":
    file1 = open('login.txt', 'r+')
    l=['username','password']
    
    dic2 = file1.read()
    dic3 = dic2.replace('][', '],[')
    dic4 = '[' + dic3 + ']'
    
    res = eval(dic4)
    global dic1
    dic1 = res.copy()
            
    #res = [ele.replace("''", "'") for ele in res]
    
    
    #dic3 = list(dic3.split(','))
    #dic1 = []

    #for i in dic3:
        
     #   dic1.append(res)
            
    #print(res, type(res))
    
    #dic1 = (dic1)
    #if __name__ == "__main__":
    global lol
    lol = MainWindow.printt()
    l = [lol[0], lol[1]]
    #print(l, type(l[1]))
    
    username_list = []
    for k in range(len(dic1)):
        username_list.append(dic1[k][0])
        
    if l[0] in username_list:
        for k in range(len(dic1)):
            if dic1[k][0] == l[0]:
                if dic1[k][1] == l[1]:
                    
                    print('Login successful')
                    details=l.copy()
                    #books_issue.open_booksissue()
                    file1 = open('storage.csv','w+')
                    reader = csv.reader(file1, delimiter=',')
                    listy=[]
                    
                    for row in reader:
                        print('row')
                        if row[1] != '':
                            listy.append(row[0])
                    
                    if lol[0] in listy:
                        return_book()
                    else:
                        issue_book()

    else:
        #if __name__ == "__main__":
        #MainWindow.invalid_login()
        #time.sleep(4)
        #MainWindow.window.withdraw()
        popup('Username Not Found', 'Username Not Found')
        
    


def register():
    RegistrationPage.open_RegistrationPage()
    
'''
def make_account():
    file1 = open('login.txt', 'w+')
    dic1 = list(file1.read())
    l = [tup[3], tup[4]]
    dic1.append(l)
    file1.write(str(l))
    file1.close()
    print('Registration successful')
    # checking login, registering users and membership details
''' 


def issue_book():
    #if __name__ == "__main__":
    books_issue.open_booksissue()
#tkinter bs here to select book from dropdown and all that
    #rn = date.today()
    #duedate = rn + timedelta(days=10)
    #print("Book must be returned before", str(duedate)) #print last return date and threaten late fees TKINTER
   # bookname = 'return in issue book function'
    #storagewrite(details[0],bookname,duedate)
    
def return_book():
    file1 = open('storage.csv','w+')
    reader = csv.reader(file1, delimiter=',')
    listy=[]
    for row in reader:
        if row[0] == details[0]:
            listy = list(row)    
    books_return.open_booksreturn(listy[0],listy[1],listy[2])
    pass


def storagewrite(username, book ,duedate):
    file = open('storage.csv', 'w+')
    #COLUMNS:- USERNAME | BOOK ISSUED | DUE DATE | 
    w = csv.writer(file, delimiter=',')
    w.writerow([username,book,duedate])
    file.close()

def switch_state(button):
    if button['state'] == NORMAL:
        button['state'] = DISABLED
        returned = True



#login()
# dont forget newline in output/input 
#event loops

#popup('Bruh')

