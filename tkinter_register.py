from tkinter import *
window=Tk() #instance of frame Tk(),display root window, manages literally everything 

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
l=['The Daughter of Time','The Big Sleep','The Spy Who Came In From the Cold','Gaudy Night','The Murder of Roger Ackroyd','Rebecca',
   'Farewell My Lovely','The Moonstone','The IPCRESS File','The Maltese Falcon','The Franchise Affair','Last Seen Wearing ...',
   'The Name of the Rose','Rogue Male','The Long Goodbye','Malice Aforethought','The Day of the Jackal','The Nine Tailors',
   'And Then There Were None','The Thirty-Nine Steps','The Collected Sherlock Holmes Short Stories (stories)','Murder Must Advertise',
   'Tales of Mystery & Imagination (stories)','The Mask of DimitriosA Coffin for Dimitrios','The Moving Toyshop','The Tiger in the Smoke',
   'The False Inspector Dew','The Woman in White','A Dark-Adapted Eye','The Postman Always Rings Twice','The Glass Key',
   'The Hound of the Baskervilles','Tinker, Tailor, Soldier, Spy',"Trent's Last Case",'From Russia, with Love','Cop Hater',
   'The Dead of Jericho','Strangers on a Train','A Judgement in Stone','The Hollow Man (UK)The Three Coffins (USA)',
   'The Poisoned Chocolates Case','A Morbid Taste for Bones','The Leper of Saint Giles','A Kiss Before Dying','The Talented Mr. Ripley',
   'Brighton Rock','The Lady in the Lake','Presumed Innocent','A Demon in My View','The Devil in Velvet','A Fatal Inversion',
   'The Journeying Boy (UK)The Case of the Journeying Boy (USA)','A Taste for Death','The Eagle Has Landed','My Brother Michael',
   'Bertie and the Tin Man','Penny Black','Game, Set & Match(Berlin Game, Mexico Set, London Match)','The Danger','Devices and Desires',
   'Under World (UK)Underworld (USA)','Nine Coaches Waiting','A Running Duck','Smallbone Deceased','The Rose of Tibet','Innocent Blood',
   'Strong Poison','Hamlet, Revenge!','A Thief of Time','A Bullet in the Ballet','Deadheads','The Third Man','The Labyrinth Makers',
   'The Berlin Memorandum (UK)The Quiller Memorandum (USA)','Beast in View','The Shortest Way to Hades','Running Blind','Twice Shy',
   'The Manchurian Candidate',"Killings at Badger's Drift (UK)The Killings at Badger's Drift (USA)",'The Beast Must Die','Gorky Park',
   'Death Comes as the End','Green for Danger','Tragedy at Law','The Collector',"Gideon's Day (UK)/Gideon of Scotland Yard (USA)",
   'The Sun Chemist','The Guns of Navarone','The Colour of Murder','Greenmantle','The Riddle of the Sands','Wobble to Death',
   'Red Harvest','The Key to Rebecca','Sadie When She Died','The Murder of the Maharajah','What Bloody Man Is That?','Shooting Script',
   'The Four Just Men']
var=StringVar()
droplist=OptionMenu(window,var,*l)
var.set('Select book you want to borrow')
droplist.config(width=15)
droplist.place(x=230,y=370)
#print(StringVar(),"sv")
#print(type(fn),"fn")

inpute = tk.StringVar()
def auto_complete():
    return inpute.get()
autoc = tkentrycomplete.AutocompleteCombobox(textvariable=inpute)
autoc.set_completion_list(l)
autoc.place(x=110, y=90)
