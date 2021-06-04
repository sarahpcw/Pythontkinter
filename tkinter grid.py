#from tkinter import *
#https://www.tutorialspoint.com/python/python_gui_programming.htm

import sqlite3
def getsqldata ():
    conn = sqlite3.connect('thingsFantastics.db')
    query = "select *  from myactors  order by actorname " 
    mydata = conn.execute(query) 
    count = 0
    resultset =[]
    for line in mydata:
        count+=1
        resultset.append(str(line))  # line is a tuple, so convert tuple to string and then add to the list
    conn.close()
    return count, resultset

############# display sql result set on a tkinter window
from tkinter import Tk
from tkinter import Label
root = Tk(  )
root.title('All actors on table myactors on thingsFantastics.db')
root.geometry("450x450")

count, resultset = getsqldata()  # calling the functions
for r in range(count):
    textline =  (resultset[r])
    textline =  (str(r)+ ": "+  textline)
    
    thingsLabel =Label( text=textline, borderwidth=1 ).grid(row=r,column=2)  # widget.grid( grid_options ), Label being the widget

root.mainloop()   

"""
this sample if on the tutorialpoints page
https://www.tutorialspoint.com/python/tk_grid.htm
for r in range(3):
   for c in range(4):
      thingsLabel    =Label( text='R%s/C%s'%(r,c),   borderwidth=1 ).grid(row=r,column=c)
#     thingsLabel.grid(row=r,column=c)
"""
