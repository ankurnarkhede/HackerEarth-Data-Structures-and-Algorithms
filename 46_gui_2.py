#----------gui----------
from Tkinter import*


top=Tk()
#--------------------------------
#adding title
top.title("ANKUR")
#attr of button
def press():
    print "U pressed button"
b=Button(top,command=press,text="lol",padx=50,pady=10,bg="yellow",fg="red",relief="flat",borderwidth="10",font=(("Pristina"),"20"),state="active")

b.config(bg="cyan")  #to add attr afterwardss

print b.cget("bg")  #to get attr

top.minsize(640,360)   #minimum sixe of window,,,,attr in px

top.configure(bg="orange")  #blue color to bg
b.pack()
#--------------------------------
top.mainloop()