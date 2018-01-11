#----------gui entry----------
from tkinter import*


top=Tk()
#--------------------------------
#adding title
top.title("ANKUR")

w=Label(top, text=("ankurr"))
top.minsize(640,360)   #minimum sixe of window,,,,attr in px

top.configure(bg="orange")  #blue color to bg
w.pack()
#--------------------------------
top.mainloop()