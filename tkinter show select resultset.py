
from PIL import ImageTk, Image
import sqlite3

from tkinter import Tk
from tkinter import Label
root = Tk(  )

root.title('Display image')
root.geometry("400x400")

load = Image.open("youtube-ico.png")
render = ImageTk.PhotoImage(load)
img = Label( image=render)
img.image = render
img.place(x=150, y=150)
textline = 'bollox'
r = 100
thingsLabel =Label( text=textline, borderwidth=1 ).grid(row=r,column=2)
r = 200
thingsLabel =Label( text=textline, borderwidth=1 ).grid(row=r,column=2)
r = 300
thingsLabel =Label( text=textline, borderwidth=1 ).grid(row=r,column=2)
r = 700
thingsLabel =Label( text=textline, borderwidth=1 ).grid(row=r,column=2)
r = 8
thingsLabel =Label( text=textline, borderwidth=1 ).grid(row=r,column=2)
r = 9
thingsLabel =Label( text=textline, borderwidth=1 ).grid(row=r,column=2)
r = 10
thingsLabel =Label( text=textline, borderwidth=1 ).grid(row=r,column=2)
r = 11
thingsLabel =Label( text=textline, borderwidth=1 ).grid(row=r,column=2)
r = 12
thingsLabel =Label( text=textline, borderwidth=1 ).grid(row=r,column=2)
r = 13
thingsLabel =Label( text=textline, borderwidth=1 ).grid(row=r,column=2)
r = 14
thingsLabel =Label( text=textline, borderwidth=1 ).grid(row=r,column=2)
r = 15
thingsLabel =Label( text=textline, borderwidth=1 ).grid(row=r,column=2)
r = 16
thingsLabel =Label( text=textline, borderwidth=1 ).grid(row=r,column=2)
r = 17
thingsLabel =Label( text=textline, borderwidth=1 ).grid(row=r,column=2)
r = 18
thingsLabel =Label( text=textline, borderwidth=1 ).grid(row=r,column=2)
r = 18
thingsLabel =Label( text=textline, borderwidth=1 ).grid(row=r,column=2)

#selects = "select *  from myactors  order by actorname " 
#query = selects  
#conn = sqlite3.connect('thingsFantastics.db')
#mydata = conn.execute(query) 
#print ( "All Actors: ")
#for line in mydata:
#    # code
#    print(line)
#conn.close()
#

root.mainloop()

"""
from tkinter import *

# pip install pillow
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = Image.open("parrot.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        
root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("200x120")
root.mainloop()
"""