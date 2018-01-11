#----------gui entry----------
from Tkinter import*

top=Tk()
#--------------------------------
top.title("ANKUR")
#-----------


#------------------------
g=Frame(top) #creating frame

Checkbutton(g,text="Option 1").pack()
Checkbutton(g,text="Option 2").pack()
Checkbutton(g,text="Option 3").pack()
Checkbutton(g,text="Option 4").pack()
Checkbutton(g,text="Option 5").pack()

#Entry(g).pack(side=RIGHT,fill=X,expand=True,padx=768)

g.pack(anchor="w")
#--------------------------
top.minsize(640,360)
top.configure(bg="#8e44ad")
#--------------------------------
top.mainloop()