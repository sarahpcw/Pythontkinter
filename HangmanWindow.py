from tkinter import Tk
from tkinter import Button
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter.constants import BOTTOM, TOP, X, W, E, LEFT
from guiFunctionsNEW import guiFunctionsNEW

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

    pwLabel.place(x=100, y=40)
    entryBox.place(x=215, y=40)

    vLength.place(x=100, y=70)
    vNr.place(x=100, y=100)
    vLower.place(x=100, y=130)
    vUpper.place(x=100, y=160)

    validationLabel.place(x=100, y=190)
    btn.place(x=100, y=250)        
 
def codeWhenClick():
    print("click submit")               #print on the console only

    getPassword = (entryBox.get())      #get the password from the entry box
    print("start", getPassword)         #print on the console only

    validation, vN, vLo, vU, vL = Window.var.calcPassword( getPassword ) #call the calcPassword function

    validationLabel.config(text="Password validation: %s" % validation) #place new message on the GUI
    vLength.config(text="Length at least 8 characters: %s" % vL)        #place new message on the GUI
    vNr.config(text="At least one number required: %s" % vN)            #place new message on the GUI
    vLower.config(text="At least one lowercase required: %s" % vLo)     #place new message on the GUI
    vUpper.config(text="At least one uppercase required: %s" % vU)      #place new message on the GUI






       
root = Tk()                                             #create object of class TKinter, that will supply functions for GUI
root.geometry("500x500")                                # Build the screen, size of the window


pwLabel =Label( text='Enter your password ')            # creating a lable element instance 
vLength =Label( text='Length validation : ')            # creating a label element instance 
vNr     =Label( text='Numbers validation : ')           # creating a label element instance 
vLower  =Label( text='Lowercase valididation: ')        # creating a label element instance 
vUpper  =Label( text='Uppercase valididation: ')        # creating a label element instance 
validationLabel=Label( text='Password valididation: ')  # creating a label element instance 
entryBox=Entry()                                        # creating an entry box element instance 
btn     =Button(text='Submit your password ',bg="orange",command=codeWhenClick)
quitBut = Button(text="Quit")                           # creating a button element instance 
    
placeElements()                                         # place elements onto the GUI
app = Window(root)
root.mainloop()
