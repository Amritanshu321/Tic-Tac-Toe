from tkinter import *
from PIL import Image,ImageTk
root=Tk()
width= root.winfo_screenwidth()
print(width)
height = root.winfo_screenheight()
print(height)


# f2=Frame(root,bg="black",borderwidth=6,padx=40)
# f2.place(x=0,y=100,width=203,height=height-100)
# f3=Frame(root,bg="black",borderwidth=6,padx=40)
# f3.place(x=203,y=100,width=height-200,height=height-100)
widthn=width-(height+3)
# f4=Frame(root,bg="black",borderwidth=6,padx=40)
# f4.place(x=height+3,y=100,width=widthn,height=height-100)

print(height-200)
def heading():
    l1 = Label(root, text="Tic Tac Toe Game", fg="black", bg="blue",
               font=("comic sans Ms", 50, "bold"),)
    l1.place(x=0,y=0,height=100,width=width)

def menu():
    l2 = Label(root, text="Menu", fg="white", bg="black",
               font=("Ariel", 30, "bold"),padx=10,pady=10)
    l2.place(x=30,y=100)

    btn = Button(root, text="Restart", bg="white", fg="black", width=27, height=5,bd=3,font=("Ariel",8, "bold"),activebackground="blue")
    btn.place(x=0,y=175)
    btn = Button(root, text="Setting", bg="white", fg="black", width=27, height=5,bd=3,font=("Ariel",8, "bold"),activebackground="blue")
    btn.place(x=0, y=260)
    btn = Button(root, text="Help", bg="white", fg="black", width=27, height=5,bd=3,font=("Ariel",8, "bold"),activebackground="blue")
    btn.place(x=0, y=345)
    btn = Button(root, text="Sound", bg="white", fg="black", width=27, height=5,bd=3,font=("Ariel",8, "bold"),activebackground="blue")
    btn.place(x=0, y=430)
    btn = Button(root, text="Close", bg="white", fg="black", width=27, height=5,bd=3,font=("Ariel",8, "bold"),activebackground="blue")
    btn.place(x=0, y=515)

def gaming_window():
    btn1 = Button(f3, text="1", font=("Ariel", 12, "bold"), bd=12, width=17, height=10)
    btn1.grid(row=0, column=0)
    btn2 = Button(f3, text="2", font=("Ariel", 12, "bold"), bd=12, width=17, height=10)
    btn2.grid(row=0, column=1)
    btn3 = Button(f3, text="3", font=("Ariel", 12, "bold"), bd=12, width=17, height=10)
    btn3.grid(row=0, column=2)
    btn4 = Button(f3, text="4", font=("Ariel", 12, "bold"), bd=12, width=17, height=10)
    btn4.grid(row=1, column=0)
    btn5 = Button(f3, text="5", font=("Ariel", 12, "bold"), bd=12, width=17, height=10)
    btn5.grid(row=1, column=1)
    btn6 = Button(f3, text="6", font=("Ariel", 12, "bold"), bd=12, width=17, height=10)
    btn6.grid(row=1, column=2)
    btn7 = Button(f3, text="7", font=("Ariel", 12, "bold"), bd=12, width=17, height=10)
    btn7.grid(row=2, column=0)
    btn8 = Button(f3, text="8", font=("Ariel", 12, "bold"), bd=12, width=17, height=10)
    btn8.grid(row=2, column=1)
    btn9 = Button(f3, text="9", font=("Ariel", 12, "bold"), bd=12, width=17, height=10)
    btn9.grid(row=2, column=2)

def scorecard():
    pass
'''
    global x
    x = 0
    x = str(x)
    l3 = Label(root, text="Score card ", fg="black",
               font=("Ariel", 40, "bold"))
    l3.place(x=height+225,y=150)
    score = "Round " + x + " / 10"

    l4 = Label(root, text=score, fg="black",
                font=("comic sans Ms", 25, "bold"))
    l4.place(x=height + 260, y=225)'''

# user_image = ImageTk.PhotoImage(Image.open('ben3.jpg'))
# label1 = Label(root, image=user_image, compound=TOP, font=('comic sans ms', 15, 'bold'))
# label1.place(x=250, y=300)
img=Image.open("bheem.png")
img=img.resize((150,300))
user_image = ImageTk.PhotoImage(img)
label1 = Label(f3, image=user_image, compound=TOP, font=('comic sans ms', 15, 'bold'))
label1.place(x=height+260,y=250)

scorecard()
root.geometry("%dx%d+0+0"%(width,height))
root.mainloop()