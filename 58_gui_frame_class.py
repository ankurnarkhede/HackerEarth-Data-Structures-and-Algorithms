#----------gui entry----------
from Tkinter import*
#-----doubts
#--------frame using class----------------
class F(Frame):
    def __init__(self,parent,label,labelwidth=12):
        Frame.__(self,parent)
        
        w1=Label(self,text=label,width=labelwidth,anchor=w)
        w1.pack(side=LEFT)

newframe=F()
        
        
        
#------------------------    
top=Tk()

find=newframe(top,'Find:')
find.pack(side=TOP,fill=X)

replace=newframe(top,'Replace:')
replace.pack(side=TOP,fill=X)

top.mainloop()