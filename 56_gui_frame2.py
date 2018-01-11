#----------gui entry----------
from Tkinter import*

top=Tk()
#--------------------------------
top.title("ANKUR")
#-----------
f=Frame(top) #creating frame

Label(f,text='Select the correct option:').pack(side=LEFT)   #widget 1

f.pack(anchor="w")

#------------------------
g=Frame(top) #creating frame

Radiobutton(g,text="Option 1").pack(side=LEFT,)
Radiobutton(g,text="Option 2").pack(side=RIGHT,)
Radiobutton(g,text="Option 3").pack(side=RIGHT,)
Radiobutton(g,text="Option 4").pack(side=RIGHT,)
Radiobutton(g,text="Option 5").pack(side=RIGHT,)

#Entry(g).pack(side=RIGHT,fill=X,expand=True,padx=768)

g.pack(anchor="w")
#--------------------------
top.minsize(640,360)
top.configure(bg="orange")
#--------------------------------
top.mainloop()