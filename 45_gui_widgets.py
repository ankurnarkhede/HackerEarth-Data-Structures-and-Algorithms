#----------gui----------

from Tkinter import*
top=Tk()
#--------------------------------
#adding title
top.title("ANKUR")
#attr of button

b=Button(top,text="lol",padx=50,pady=10,bg="yellow",fg="red",relief="flat",borderwidth="10",font=(("Pristina"),"20"),state="active")

top.minsize(640,360)   #minimum sixe of window,,,,attr in px

top.configure(bg="orange")  #blue color to bg
b.pack()
#--------------------------------
top.mainloop()