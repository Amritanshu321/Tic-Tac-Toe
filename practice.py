from tkinter import *
from datetime import *
root=Tk()
width= root.winfo_screenwidth()
print(width)
height = root.winfo_screenheight()
print(height)
def mainheading():
    # mainframe=Frame(root)
    # mainframe.grid(row=0,columnspan=4)
    label = Label(root, text="Tic Tac Toe Game", fg="black", bg="blue",
                  font=("comic sans Ms", 45, "bold"))
    label.grid(row=0,columnspan=4,padx=500, pady=0)

def menu():
    # f1=Frame(root,bg="black")
    # f1.grid(row=1,column=0)
    label = Button(root, text="Menu", fg="black", bg="blue",
                  font=("comic sans Ms", 45, "bold"))
    label.grid(row=1, columnspan=4, padx=0,pady=0)
    #btn = Button(f1, text="Restart", bg="white", fg="black", width=10, height=5)
    #btn.grid(row=1,column=0,padx=0,pady=10)
    #
    #
    # btn = Button(f1, text="Help", bg="white", fg="black", width=10, height=5)
    # btn.grid(row=2,column=0,padx=0,pady=10)
    #
    # btn = Button(f1, text="Setting", bg="white", fg="black", width=10, height=5)
    # btn.grid(row=3,column=0,padx=0,pady=10)
    #
    # btn = Button(f1, text="Exit", bg="white", fg="black", width=10, height=5)
    # btn.grid(row=4,column=0,padx=0,pady=10)

menu()
mainheading()
#mainwindow()
root.title("Tic Tac Toe Game")
root.geometry("%dx%d+0+0"%(width,height))
root.mainloop()