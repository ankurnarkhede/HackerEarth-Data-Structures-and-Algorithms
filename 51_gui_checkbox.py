#----------gui entry----------
from Tkinter import*


top=Tk()
#--------------------------------
#adding title
top.title("ANKUR")

mode=IntVar()
w=Checkbutton(top,text="Debug mode",variable=mode)
print mode.get()


top.minsize(640,360)   #minimum sixe of window,,,,attr in px
top.configure(bg="orange")  #blue color to bg
w.pack()
#--------------------------------
top.mainloop()