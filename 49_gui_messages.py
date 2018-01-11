#----------gui entry----------
from Tkinter import*


top=Tk()
#--------------------------------
#adding title
top.title("ANKUR")

w=Message(top,text="this is a message",padx=70,pady=70)
top.minsize(640,360)   #minimum sixe of window,,,,attr in px

top.configure(bg="orange")  #blue color to bg
w.pack()
#--------------------------------
top.mainloop()