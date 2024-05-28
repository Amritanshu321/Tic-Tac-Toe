from tkinter import *
from datetime import *
root=Tk()
width= root.winfo_screenwidth()
print(width)
height = root.winfo_screenheight()
print(height)

def mainheading():
    mainframe=Frame(root)
    mainframe.grid(row=0,columnspan=4)
    label = Label(mainframe, text="Tic Tac Toe Game", fg="black", bg="blue",
                  font=("comic sans Ms", 45, "bold"), padx=500, pady=0)
    label.grid(row=0,column=0)

def mainwindow():
    ff = Frame(root)
    #ff.place(x=0,y=100)
    ff.grid(row=1,columnspan=4)


mainheading()
mainwindow()
root.title("Tic Tac Toe Game")
root.geometry("%dx%d+0+0"%(width,height))
root.mainloop()