#----------gui entry----------
from tkinter import*


top=Tk()
#--------------------------------
top.title("ANKUR")

w1=Button(top,text="tiny")
w2=Button(top,text="very very big")
w3=Button(top,text="very very big",bg='yellow')


top.config(bg="orange")
w1.pack(side=TOP,fill=X)#filling x dir
w2.pack(side=TOP,fill=X)
w3.pack(side=TOP,fill=BOTH,expand=True) #filling in both x and y dir

#--------------------------------
top.mainloop()