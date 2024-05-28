from tkinter import *
from datetime import *
from PIL import Image,ImageTk
root=Tk()
width= root.winfo_screenwidth()
print(width)
height = root.winfo_screenheight()
print(height)
f1=Frame(root,bg="blue",borderwidth=6)
f2=Frame(root,bg="black",borderwidth=6,padx=40)
fm=Frame(root,borderwidth=6,bg="black")
f3=Frame(root,borderwidth=6)
f4=Frame(root,bg="yellow",borderwidth=6)

f1.pack(side=TOP,fill="x")
f2.pack(side=LEFT,fill="y")
fm.pack(side=LEFT,fill="y")
f3.pack(side=LEFT,fill="both")
f4.pack(side=BOTTOM,fill="x")

###### heading##########
def heading():
    l1 = Label(f1, text="Tic Tac Toe Game", fg="black", bg="blue",
               font=("comic sans Ms", 30, "bold"))
    l1.pack(pady=20)



#########for menu###########
def menu():
    '''
    l1=Label(f2,text="Menu",fg="white", bg="black",
                      font=("Ariel", 10, "bold"))
    #l1.pack(padx=0,fill="y")
    l1.grid(row=0,column=0,padx=0)
    '''
    btn = Button(f2, text="Restart", bg="white", fg="black", width=10, height=5)
    # btn.grid(row=1,columnspan=2)
    btn.pack(side=TOP, fill="x")

    btn = Button(f2, text="Help", bg="white", fg="black", width=10, height=5)
    btn.pack(side=TOP, fill="x")

    btn = Button(f2, text="Setting", bg="white", fg="black", width=10, height=5)
    btn.pack(side=TOP, fill="x")

    btn = Button(f2, text="Exit", bg="white", fg="black", width=10, height=5)
    btn.pack(side=TOP, fill="x")



######## for Main gaming Window #########
def gaming_window():
    btn1 = Button(fm, text="1", font=("Ariel", 12, "bold"), bd=12,width=15,height=10)
    btn1.grid(row=0, column=0)
    btn2 = Button(fm, text="2", font=("Ariel", 12, "bold"), bd=12,width=15,height=10)
    btn2.grid(row=0, column=1)
    btn3 = Button(fm, text="3", font=("Ariel", 12, "bold"), bd=12,width=15,height=10)
    btn3.grid(row=0, column=2)
    btn4 = Button(fm, text="4", font=("Ariel", 12, "bold"), bd=12,width=15,height=10)
    btn4.grid(row=1, column=0)
    btn5 = Button(fm, text="5", font=("Ariel", 12, "bold"), bd=12,width=15,height=10)
    btn5.grid(row=1, column=1)
    btn6 = Button(fm, text="6", font=("Ariel", 12, "bold"), bd=12,width=15,height=10)
    btn6.grid(row=1, column=2)
    btn7 = Button(fm, text="7", font=("Ariel", 12, "bold"), bd=12, width=15, height=10)
    btn7.grid(row=2, column=0)
    btn8 = Button(fm, text="8", font=("Ariel", 12, "bold"), bd=12, width=15, height=10)
    btn8.grid(row=2, column=1)
    btn9 = Button(fm, text="9", font=("Ariel", 12, "bold"), bd=12, width=15, height=10)
    btn9.grid(row=2, column=2)
######### score card#########
def Scorecard():
    global x
    x=0
    x=str(x)
    l2 = Label(f3, text="Score card ", fg="black",
               font=("comic sans Ms", 30, "bold"))
    l2.pack(side=TOP,padx=250,pady=20)
    score="Round "+x+" / 10"

    l3 = Label(f3, text=score, fg="black",
               font=("comic sans Ms", 30, "bold"))
    #l3.pack(side=TOP, padx=250, pady=5)

    img=Image.open("ben1.png")
    img=img.resize((150,300))
    user_image = ImageTk.PhotoImage(img)
    label1 = Label(f3, image=user_image, compound=TOP, font=('comic sans ms', 15, 'bold'))
    label1.pack(side=RIGHT, padx=250, pady=5)

    #login_image = ImageTk.PhotoImage(Image.open('log.jpg'))

heading()
menu()
gaming_window()
Scorecard()
root.title("Tic Tac Toe Game")
root.geometry("%dx%d+0+0"%(width,height))
root.mainloop()