#----------gui entry----------
from Tkinter import*
import tkMessageBox as ms

top=Tk()
#--------------------------------
#adding title
top.title("ANKUR")

def hello():
    ms.showinfo("msg box title","msg box text")

w=Button(top,text='A button',command=hello)


top.minsize(640,360)   #minimum sixe of window,,,,attr in px
top.configure(bg="orange")  #blue color to bg
w.pack()
#--------------------------------
top.mainloop()