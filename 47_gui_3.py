#----------gui entry----------
from Tkinter import*


top=Tk()
#--------------------------------
#adding title
top.title("ANKUR")
#attr of button

s=StringVar()
w=Entry(top,textvariable=s)


print s.get()
top.minsize(640,360)   #minimum sixe of window,,,,attr in px

top.configure(bg="orange")  #blue color to bg
w.pack()
#--------------------------------
top.mainloop()