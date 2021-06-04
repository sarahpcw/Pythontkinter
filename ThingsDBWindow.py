from tkinter import Tk
from tkinter import ttk
from tkinter import Button
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Checkbutton
#from tkinter import Combobox
#from tkinter import IntVar
from tkinter import StringVar
from tkinter.constants import BOTTOM, TOP, X, W, E, LEFT
from guiFunctionsNEW import guiFunctionsNEW
from thingsdbmaintenance import thingsdbmaintenance
obj = thingsdbmaintenance()

class Window(Frame):  
    var = list()
    
    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()
        Window.var = guiFunctionsNEW()
        
    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Testing GUI - Password app")

        # allowing the widget to take the full space of the root window
        self.pack(side=TOP, fill=X, expand=1)

def placeElements ():   
    # placing the elements on my window
    quitBut.place(x=10, y=10)  
    
    cboxCrime.place(x=100   ,y=40)
    cboxRomance.place(x=200 ,y=40)
    cboxThriller.place(x=300,y=40)
    cboxAction.place(x=100  ,y=70)
    cboxFantasy.place(x=200 ,y=70)
    cboxFamily.place(x=300  ,y=70)
    cboxComedy.place(x=100  ,y=100)
    cboxBioPic.place(x=200  ,y=100)
    cboxTrueStory.place(x=300,y=100)
 
    thingsLabel.place(x=100, y=140)
    entryBox.place(x=215, y=140)

    vLength.place(x=100, y=170)
    dropListActor.place ( x = 250, y = 170)
    vNr.place(x=100, y=200)
    vLower.place(x=100, y=230)
    vUpper.place(x=100, y=260)

    validationLabel.place(x=100, y=290)
    btn.place(x=100, y=330)        
 
def codeWhenClick():
    print("click submit")               #print on the console only
    
############### this is tickboxes for genres to be associated with the new movie
    getCrime    = (varCrime.get())      
    getRomance  = (varRomance.get())  
    getThriller = (varThriller.get())  
    getAction   = (varAction.get())   
    getFantasy  = (varFantasy.get())   
    getFamily   = (varFamily.get())   
    getComedy   = (varComedy.get())  
    getBioPic   = (varBioPic.get())   
    getTrueStory= (varTrueStory.get())  
    getActor    = (varActor.get())
    print ('getactor',getActor)
    getActor = dropListActor.bind("<<ComboboxSelected>>", callbackFunc)
    
    
    # this is tickboxes for genres to be associated with the new movie
    newCatsName = getCrime +","+ getRomance +","+ getThriller +","+ getAction +","+ getFantasy +","+ getFamily +","+ getComedy +","+ getBioPic +","+ getTrueStory 
    while (newCatsName.startswith(',')) :
        newCatsName = newCatsName[1:]
    while (newCatsName.endswith(',')):
        newCatsName = newCatsName[:-1]
    while  ',,' in newCatsName :
        newCatsName = newCatsName.replace(',,',',')
    print ( newCatsName )
    ###############   
    print("", getCrime)       #### add each of there names to the mycats table , use the insert function
    print("", getRomance)     #### add each
    print("", getThriller)    #### add each
    print("", getAction)      #### add each
    print("", getFantasy)     #### add each
    print("", getFamily)      #### add each
    print("", getComedy)      #### add each
    print("", getBioPic)      #### add each
    print("", getTrueStory)   #### add each 
    obj.insertCatsTable( getCrime ) 
    obj.insertCatsTable( getRomance)     #### add each to db mycats table, if not yet there
    obj.insertCatsTable( getThriller)    #### add each
    obj.insertCatsTable( getAction)      #### add each
    obj.insertCatsTable( getFantasy)     #### add each
    obj.insertCatsTable( getFamily)      #### add each
    obj.insertCatsTable( getComedy)      #### add each
    obj.insertCatsTable( getBioPic)      #### add each
    obj.insertCatsTable( getTrueStory)   #### add each
############### end of tickboxes
    
############### actor drop list
    
############### drop list

##############    get , evaluate and report on the password, change to thingname
    getThingsName = (entryBox.get())      #get the password from the entry box - change to thingname
    print("Thing name given", getThingsName )
    obj.findThingAdd(getThingsName, newCatsName, 'peter') 
#    obj.showThingsAll()
#    obj.showCatsAll()
#    obj.showActorsAll()
    ################ call the insert function and 
    ################ add the thing name to the things table, with the newCatsName and actor
"""
    ## evaluate the password
    validation, vN, vLo, vU, vL = Window.var.calcPassword( getThingsName ) #call the calcPassword function
    ## report the password evaluation
    validationLabel.config(text="Password validation: %s" % validation) #place new message on the GUI
    vLength.config(text="Length at least 8 characters: %s" % vL)        #place new message on the GUI
    vNr.config(text="At least one number required: %s" % vN)            #place new message on the GUI
    vLower.config(text="At least one lowercase required: %s" % vLo)     #place new message on the GUI
    vUpper.config(text="At least one uppercase required: %s" % vU)      #place new message on the GUI
##############    finished with the password

"""




       
root = Tk()                                             #create object of class TKinter, that will supply functions for GUI
root.geometry("500x500")                                # Build the screen, size of the window

thingsLabel    =Label( text='Enter your password ')            # creating a lable element instance 
vLength        =Label( text='Length validation : ')            # creating a label element instance 
vNr            =Label( text='Numbers validation : ')           # creating a label element instance 
vLower         =Label( text='Lowercase valididation: ')        # creating a label element instance 
vUpper         =Label( text='Uppercase valididation: ')        # creating a label element instance 
validationLabel=Label( text='Password valididation: ')  # creating a label element instance 

varCrime      = StringVar()
cboxCrime     = Checkbutton( text="Crime", variable=varCrime, onvalue="Crime",offvalue="")
varRomance    = StringVar()
cboxRomance   = Checkbutton( text="Romance", variable=varRomance, onvalue="Romance",offvalue="")
varThriller   = StringVar()
cboxThriller  = Checkbutton( text="Thriller", variable=varThriller, onvalue="Thriller",offvalue="")
varAction     = StringVar()
cboxAction    = Checkbutton( text="Action", variable=varAction, onvalue="Action",offvalue="")
varFantasy    = StringVar()
cboxFantasy   = Checkbutton( text="Fantasy", variable=varFantasy, onvalue="Fantasy",offvalue="")
varFamily     = StringVar()
cboxFamily    = Checkbutton( text="Family", variable=varFamily, onvalue="Family",offvalue="")
varComedy     = StringVar()
cboxComedy    = Checkbutton( text="Comedy", variable=varComedy, onvalue="Comedy",offvalue="")
varBioPic     = StringVar()
cboxBioPic    = Checkbutton( text="BioPic", variable=varBioPic, onvalue="BioPic",offvalue="")
varTrueStory  = StringVar()
cboxTrueStory = Checkbutton( text="TrueStory", variable=varTrueStory, onvalue="TrueStory",offvalue="")

varActor= StringVar()
dropListActor = ttk.Combobox ( value = ['alpna','nano'] )


def callbackFunc(event):
    print("New Element Selected")
    selected=event
    print(selected)
    return selected
    
PARKING_LOTS = ('ARTX', 'BURG', 'CLAY_HALL', 'GLAB', 'HAMH_HUTC',
                    'HHPA', 'JVIC', 'LIBR', 'PLSU', 'POST', 'PROF',
                    'STEC', 'STRO_NORTH', 'STRO_WEST', 'TROP')

#w = Listbox( option=value ) 
actorDropList = ttk.Combobox ( value = ['alpna','nano'] )
print("Drop List values current", actorDropList.current(), "Drop List values get", actorDropList.get())
a = StringVar()
a = actorDropList.bind("<<ComboboxSelected>>", callbackFunc)
print ( actorDropList.get() )
if actorDropList.get() == "ARTX":
    print ( "drop value " , "ARTX")
    
#a = actorDropList.bind("<Control-a>",lambda e: (actorDropList.select_range(0,ttk.END),"break")[1])
print ( 'a----------',a)

entryBox=Entry()                                        # creating an entry box element instance 
btn     =Button(text='Submit your password ',bg="orange",command=codeWhenClick)
quitBut = Button(text="Quit")                           # creating a button element instance 
    
placeElements()                                         # place elements onto the GUI
app = Window(root)
root.mainloop()
