#----------gui entry----------
from Tkinter import*


top=Tk()
#--------------------------------
#adding title
top.title("ANKUR")

def submit():
    print ("u selected option", fav.get())
    #prints in console

fav=IntVar()
r1=Radiobutton(top,text="python",variable=fav,value=1,command=submit, padx=50,pady=10)
r2=Radiobutton(top,text="c",variable=fav,value=2,command=submit, padx=50,pady=10)
r3=Radiobutton(top,text="java",variable=fav,value=3,command=submit, padx=50,pady=10)

#value is  stored in variable=fav...then get the value by fav.get()

top.minsize(640,360)   #minimum sixe of window,,,,attr in px
top.configure(bg="orange")  #blue color to bg
r1.pack()
r2.pack()
r3.pack()

v=Label(top)

#--------------------------------
top.mainloop()