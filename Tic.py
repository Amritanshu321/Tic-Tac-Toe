from tkinter import *
from datetime import *
from PIL import Image,ImageTk
import tkinter.font as fo
from tkinter import messagebox
from pygame import mixer
root=Tk()
width= root.winfo_screenwidth()
print(width)
height = root.winfo_screenheight()
print(height)

count=1
b1,b2,b3,b4,b5,b6,b7,b8,b9=0,0,0,0,0,0,0,0,0
score0=0
scorex=0
y="0"
score = "Round " + y + " / 10"
global win,evenwin
win=0
evenwin=0
global gaming_window
print(b1,b2,b3,b4,b5,b6,b7,b8,b9)
font=fo.Font(family="Helvetica",size=20,weight='bold')

f2=Frame(root,bg="black",borderwidth=6,padx=40)
f2.place(x=0,y=100,width=203,height=height-100)
f3=Frame(root,bg="black",borderwidth=6,padx=40)
f3.place(x=203,y=100,width=height-200,height=height-100)
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

    btn = Button(root, text="Restart", bg="white", fg="black", width=27, height=5,bd=3,font=("Ariel",8, "bold"),activebackground="blue",command=startNew)
    btn.place(x=0,y=175)
    btn = Button(root, text="Setting", bg="white", fg="black", width=27, height=5,bd=3,font=("Ariel",8, "bold"),activebackground="blue",command=setting)
    btn.place(x=0, y=260)
    btn = Button(root, text="Help", bg="white", fg="black", width=27, height=5,bd=3,font=("Ariel",8, "bold"),activebackground="blue",command=helpwindow)
    btn.place(x=0, y=345)
    btn = Button(root, text="Sound", bg="white", fg="black", width=27, height=5,bd=3,font=("Ariel",8, "bold"),activebackground="blue",command=Sound)
    btn.place(x=0, y=430)
    btn = Button(root, text="Close", bg="white", fg="black", width=27, height=5,bd=3,font=("Ariel",8, "bold"),activebackground="blue",command=quit)
    btn.place(x=0, y=515)
    btn = Button(root, text="Exit", bg="white", fg="black", width=27, height=5, bd=3, font=("Ariel", 8, "bold"),
                 activebackground="blue",command=quit)
    btn.place(x=0, y=600)

def setting():
    messagebox.showinfo("Setting","Do not open this again This is a harmful Setting")
def helpwindow():
    top = Toplevel()  # to open new window
    top.title("Help Window")
    top.geometry("400x200+150+100")
    lab=Label(top,text="This is the Help window for tic tac toe game",font=("Ariel",15, "bold"),bg="red").pack(side=TOP,fill="x")
    lab1=Label(top,text="first player will always click first in all rounds",font=("Ariel",8, "bold")).pack(side=TOP,fill="x")
    btn_destroy = Button(top, text="close Window",font=("Ariel",8, "bold"), command=top.destroy,bg="green").pack(side=BOTTOM,fill="x")

def gaming_window():
    global btn1
    btn1 = Button(f3, text="1", font=("Ariel", 65, "bold"),fg="black", bd=12, width=3, height=1,command=msg1)
    btn1.grid(row=0, column=0)
    global btn2
    btn2 = Button(f3, text="2", font=("Ariel", 65, "bold"), bd=12, width=3, height=1,command=msg2)
    btn2.grid(row=0, column=1)
    global btn3
    btn3 = Button(f3, text="3", font=("Ariel", 65, "bold"), bd=12, width=3, height=1,command=msg3)
    btn3.grid(row=0, column=2)
    global btn4
    btn4 = Button(f3, text="4", font=("Ariel", 65, "bold"), bd=12, width=3, height=1,command=msg4)
    btn4.grid(row=1, column=0)
    global btn5
    btn5 = Button(f3, text="5", font=("Ariel", 65, "bold"), bd=12, width=3, height=1,command=msg5)
    btn5.grid(row=1, column=1)
    global btn6
    btn6 = Button(f3, text="6", font=("Ariel", 65, "bold"), bd=12, width=3, height=1,command=msg6)
    btn6.grid(row=1, column=2)
    global btn7
    btn7 = Button(f3, text="7", font=("Ariel", 65, "bold"), bd=12, width=3, height=1,command=msg7)
    btn7.grid(row=2, column=0)
    global btn8
    btn8 = Button(f3, text="8", font=("Ariel", 65, "bold"), bd=12, width=3, height=1,command=msg8)
    btn8.grid(row=2, column=1)
    global btn9
    btn9 = Button(f3, text="9", font=("Ariel", 65, "bold"), bd=12, width=3, height=1,command=msg9)
    btn9.grid(row=2, column=2)

def Scorecard():

    global x
    global score
    global y
    x = 1
    y = str(x)
    l3 = Label(root, text="Score card ", fg="black",
               font=("Ariel", 40, "bold"))
    l3.place(x=height+225,y=150)
    score = "Round " + y + " / 5"
    global l4

    l4 = Label(root, text=score, fg="black",
                font=("comic sans Ms", 25, "bold"))
    l4.place(x=height + 260, y=225)

    l5=Label(root,text="Player 0",fg="black",font=("Ariel",20,"bold"))
    l5.place(x=height+280,y=350)
    global l7
    l7 =Label(root, text=score0, fg="black", font=("Ariel", 20, "bold"))
    l7.place(x=height + 425, y=350)

    l6 = Label(root, text="Player X", fg="black", font=("Ariel", 20, "bold"))
    l6.place(x=height + 280, y=400)
    global l8

    l8 = Label(root, text=scorex, fg="black", font=("Ariel", 20, "bold"))
    l8.place(x=height + 425, y=400)

def check_even_fun():
    global scorex
    global res
    global score
    global x,y,win,evenwin
    if b1 == b2== b3==2:
        win=1
        print("x is win at 1")
        btn1.config(bg="blue")
        btn2.config(bg="blue")
        btn3.config(bg="blue")
        scorex +=1
        l8.config(text=scorex)
        res=messagebox.showinfo("Result for this round","player x is winner")
        x += 0
        y = str(x)
        l4.config(text="Round " + y + " / 5")
        nextRound()

    if b4 == b5 == b6==2:
        win = 1
        print("x is win at 2")
        btn4.config(bg="blue")
        btn5.config(bg="blue")
        btn6.config(bg="blue")
        scorex += 1
        l8.config(text=scorex)
        res = messagebox.showinfo("Result for this round", "player x is winner")
        x +=1
        y = str(x)
        l4.config(text="Round " + y + " / 5")
        nextRound()
    if b7 == b8 == b9==2:
        win = 1
        print("x is win at 3")
        btn7.config(bg="blue")
        btn8.config(bg="blue")
        btn9.config(bg="blue")
        scorex += 1
        l8.config(text=scorex)
        res = messagebox.showinfo("Result for this round", "player x is winner")
        x +=1
        y = str(x)
        l4.config(text="Round " + y + " / 5")
        nextRound()
    if b1 == b4 == b7==2:
        win = 1
        print("x is win at 4")
        btn1.config(bg="blue")
        btn4.config(bg="blue")
        btn7.config(bg="blue")
        scorex += 1
        l8.config(text=scorex)
        res = messagebox.showinfo("Result for this round", "player x is winner")
        x +=1
        y= str(x)
        l4.config(text="Round " + y + " / 5")
        nextRound()
    if b2 == b5 == b8==2:
        win = 1
        print("x is win at 5")
        btn2.config(bg="blue")
        btn5.config(bg="blue")
        btn8.config(bg="blue")
        scorex += 1
        l8.config(text=scorex)
        res = messagebox.showinfo("Result for this round", "player x is winner")
        x += 1
        y = str(x)
        l4.config(text="Round " + y + " / 5")
        nextRound()
    if b3 == b6 == b9==2:
        win = 1
        print("x is win at 6")
        btn3.config(bg="blue")
        btn6.config(bg="blue")
        btn9.config(bg="blue")
        scorex += 1
        l8.config(text=scorex)
        res = messagebox.showinfo("Result for this round", "player x is winner")
        x += 1
        y= str(x)
        l4.config(text="Round " + y + " / 5")
        nextRound()
    if b1 == b5 == b9==2:
        win = 1
        print("x is win at 7")
        btn1.config(bg="blue")
        btn5.config(bg="blue")
        btn9.config(bg="blue")
        scorex += 1
        l8.config(text=scorex)
        res = messagebox.showinfo("Result for this round", "player x is winner")
        x += 1
        y= str(x)
        l4.config(text="Round " + y + " / 5")
        nextRound()
    if b7 == b5 == b3==2:
        win = 1
        print("x is win at 8")
        btn7.config(bg="blue")
        btn5.config(bg="blue")
        btn3.config(bg="blue")
        scorex += 1
        l8.config(text=scorex)
        res = messagebox.showinfo("Result for this round", "player x is winner")
        x += 1
        y = str(x)
        l4.config(text="Round " + y + " / 5")
        nextRound()
    if count==10:
        if win==0:
            res = messagebox.showinfo("Result for this round", "No one  is winner")
            x += 1
            y = str(x)
            l4.config(text="Round " + y + " / 5")
            nextRound()
            evenwin=1
    #     res = messagebox.showinfo("Result for this round", "No one is winner in this round")


def check_odd_fun():
    global score0
    global x,y,win,evenwin
    score = "Round " + y + " / 5"

    if b1 == b2 == b3 == 1:
        win = 1
        print("0 is win at 1")
        btn1.config(bg="blue")
        btn2.config(bg="blue")
        btn3.config(bg="blue")
        score0 +=1
        l7.config(text=score0)
        res = messagebox.showinfo("Result for this round", "Player 0 is winner in this round")
        x += 1
        y = str(x)
        print(type(x))
        print(x)
        print(y)
        print(score)
        l4.config(text="Round " + y + " / 5")
        nextRound()
        #gaming_window()
        print(res)
    if b4== b5 == b6 == 1:
        win = 1
        print("0 is win at 2")
        btn4.config(bg="blue")
        btn5.config(bg="blue")
        btn6.config(bg="blue")
        score0 += 1
        l7.config(text=score0)
        res = messagebox.showinfo("Result for this round", "Player 0 is winner in this round")
        x += 1
        y= str(x)
        l4.config(text="Round " + y + " / 5")
        nextRound()
    if b7 == b8 == b9 == 1:
        win = 1
        print("0 is win at 3")
        btn7.config(bg="blue")
        btn8.config(bg="blue")
        btn9.config(bg="blue")
        score0 += 1
        l7.config(text=score0)
        res = messagebox.showinfo("Result for this round", "Player 0 is winner in this round")
        x += 1
        y = str(x)
        l4.config(text="Round " + y + " / 5")
        nextRound()
    if b1 == b4 == b7 == 1:
        win = 1
        print("0 is win at 4")
        btn1.config(bg="blue")
        btn4.config(bg="blue")
        btn7.config(bg="blue")
        score0 += 1
        l7.config(text=score0)
        res = messagebox.showinfo("Result for this round", "Player 0 is winner in this round")
        x += 1
        y = str(x)
        l4.config(text="Round " + y + " / 5")
        nextRound()
    if b2 == b5 == b8 == 1:
        win = 1
        print("0 is win at 5")
        btn2.config(bg="blue")
        btn5.config(bg="blue")
        btn8.config(bg="blue")
        score0 += 1
        l7.config(text=score0)
        res = messagebox.showinfo("Result for this round", "Player 0 is winner in this round")
        x += 1
        y = str(x)
        l4.config(text="Round " + y + " / 5")
        nextRound()
    if b3 == b6== b9 == 1:
        win = 1
        print("0 is win at 6")
        btn3.config(bg="blue")
        btn6.config(bg="blue")
        btn9.config(bg="blue")
        score0 += 1
        l7.config(text=score0)
        res = messagebox.showinfo("Result for this round", "Player 0 is winner in this round")
        x += 1
        y = str(x)
        l4.config(text="Round " + y + " / 5")
        nextRound()
    if b1 == b5 == b9 == 1:
        win = 1
        print("0 is win at 7")
        btn1.config(bg="blue")
        btn5.config(bg="blue")
        btn9.config(bg="blue")
        score0 += 1
        l7.config(text=score0)
        res = messagebox.showinfo("Result for this round", "Player 0 is winner in this round")
        x += 1
        y = str(x)
        l4.config(text="Round " + y + " / 5")
        nextRound()
    if b7 == b5 == b3 == 1:
        win = 1
        print("0 is win at 8")
        btn7.config(bg="blue")
        btn5.config(bg="blue")
        btn3.config(bg="blue")
        score0 += 1
        l7.config(text=score0)
        res = messagebox.showinfo("Result for this round", "Player 0 is winner in this round")
        x += 1
        y= str(x)
        l4.config(text="Round " + y + " / 5")
        nextRound()
    if count==10:
         if win==0:
             if evenwin==0:
                 print("no one is winner")

def msg1(e=""):
    global count
    global b1
    buttonsound()
    if count%2==0:
        b1=2
        count+=1
        btn1.config(text="x",fg="yellow",state=DISABLED)
        print(b1, b2, b3, b4, b5, b6, b7, b8, b9)
        check_even_fun()
        check_odd_fun()

    else:
        b1=1
        count+=1
        btn1.config( text="0",fg="red",state=DISABLED)
        print(b1, b2, b3, b4, b5, b6, b7, b8, b9)
        check_even_fun()
        check_odd_fun()


def msg2(e=""):
    buttonsound()
    global count
    global b2
    if count % 2 == 0:
        b2 = 2
        count += 1
        btn2.config( text="x", state=DISABLED)
        print(b1, b2, b3, b4, b5, b6, b7, b8, b9)
        check_even_fun()
        check_odd_fun()

    else:
        b2 = 1
        count += 1
        btn2.config( text="0", state=DISABLED)
        print(b1, b2, b3, b4, b5, b6, b7, b8, b9)
        check_even_fun()
        check_odd_fun()


def msg3(e=""):
    buttonsound()
    global count
    global b3
    if count % 2 == 0:
        b3 = 2
        count += 1
        btn3.config(text="x", state=DISABLED)
        print(b1,b2,b3,b4,b5,b6,b7,b8,b9)
        check_even_fun()
        check_odd_fun()

    else:
        b3 = 1
        count += 1
        btn3.config(text="0", state=DISABLED)
        print(b1,b2,b3,b4,b5,b6,b7,b8,b9)
        check_even_fun()
        check_odd_fun()


def msg4(e=""):
    buttonsound()
    global count
    global b4
    if count % 2 == 0:
        b4 = 2
        count += 1
        btn4.config(text="x",state=DISABLED)
        print(b1, b2, b3, b4, b5, b6, b7, b8, b9)
        check_even_fun()
        check_odd_fun()


    else:
        b4 = 1
        count += 1
        btn4.config(text="0", state=DISABLED)
        print(b1, b2, b3, b4, b5, b6, b7, b8, b9)
        check_even_fun()
        check_odd_fun()


def msg5(e=""):
    buttonsound()
    global count
    global b5
    if count % 2 == 0:
        b5 = 2
        count += 1
        btn5.config(text="x", state=DISABLED)
        print(b1, b2, b3, b4, b5, b6, b7, b8, b9)
        check_even_fun()
        check_odd_fun()

    else:
        b5 = 1
        count += 1
        btn5.config(text="0", state=DISABLED)
        print(b1, b2, b3, b4, b5, b6, b7, b8, b9)
        check_even_fun()
        check_odd_fun()


def msg6(e=""):
    buttonsound()
    global count
    global b6
    if count % 2 == 0:
        b6 = 2
        count += 1
        btn6.config(text="x", state=DISABLED)
        print(b1, b2, b3, b4, b5, b6, b7, b8, b9)
        check_even_fun()
        check_odd_fun()

    else:
        b6 = 1
        count += 1
        btn6.config(text="0",state=DISABLED)
        print(b1, b2, b3, b4, b5, b6, b7, b8, b9)
        check_even_fun()
        check_odd_fun()


def msg7(e=""):
    buttonsound()
    global count
    global b7
    if count % 2 == 0:
        b7 = 2
        count += 1
        btn7.config(text="x",state=DISABLED)
        print(b1, b2, b3, b4, b5, b6, b7, b8, b9)
        check_even_fun()
        check_odd_fun()

    else:
        b7 = 1
        count += 1
        btn7.config(text="0",state=DISABLED)
        print(b1, b2, b3, b4, b5, b6, b7, b8, b9)
        check_even_fun()
        check_odd_fun()


def msg8(e=""):
    buttonsound()
    global count
    global b8
    if count % 2 == 0:
        b8 = 2
        count += 1
        btn8.config(text="x", state=DISABLED)
        print(b1, b2, b3, b4, b5, b6, b7, b8, b9)
        check_even_fun()
        check_odd_fun()

    else:
        b8 = 1
        count += 1
        btn8.config( text="0", state=DISABLED)
        print(b1, b2, b3, b4, b5, b6, b7, b8, b9)
        check_even_fun()
        check_odd_fun()


def msg9(e=""):
    buttonsound()
    global count
    global b9
    if count % 2 == 0:
        b9 = 2
        count += 1
        btn9.config(text="x", state=DISABLED)
        print(b1, b2, b3, b4, b5, b6, b7, b8, b9)
        check_even_fun()
        check_odd_fun()

    else:
        b9 = 1
        count += 1
        btn9.config(text="0", state=DISABLED)
        print(b1, b2, b3, b4, b5, b6, b7, b8, b9)
        check_even_fun()
        check_odd_fun()
def playsound():
    mixer.init()
    mixer.music.load('snecky.mp3')
    mixer.music.play(-1)

def buttonsound():
    button_sound=mixer.Sound('button-3.wav')
    button_sound.play()
def stopsound():
    mixer.music.stop()
def setvolume():
    mixer.music.set_volume(0.5)

def Sound():
    top = Toplevel()  # to open new window
    top.title("Volume Setting")
    top.geometry("200x200+150+100")
    lab = Label(top, text="This is the Volume Setting ", font=("Ariel", 10, "bold"), bg="red").pack(
        side=TOP, fill="x")
    playbutton=Button(top,text="Sound ON",font=("Ariel", 8, "bold"),command=playsound).pack(side=TOP)
    pausebutton = Button(top, text="Sound OFF", font=("Ariel", 8, "bold"),command=stopsound).pack(side=TOP)
    setVol = Button(top, text="Volume Level", font=("Ariel", 8, "bold"), command=setvolume).pack(side=TOP)
    btn_destroy = Button(top, text="close Window", font=("Ariel", 8, "bold"), command=top.destroy, bg="green").pack(side=BOTTOM)

img=Image.open("ben8.png")
img=img.resize((200,450))
user_image = ImageTk.PhotoImage(img)
label1 = Label(root, image=user_image, compound=TOP, font=('comic sans ms', 15, 'bold'))
label1.place(x=height+50,y=250)

img2=Image.open("ben11.jpg")
img2=img.resize((200,450))
user_image2 = ImageTk.PhotoImage(img2)
label2 = Label(root, image=user_image2, compound=TOP, font=('comic sans ms', 15, 'bold'))
label2.place(x=height+450,y=250)

def startNew():
    global score0,scorex
    scorex=0
    score0=0
    playsound()


    heading()
    menu()
    gaming_window()
    Scorecard()

def nextRound():
    global x,res1
    if x<=5:
        global count, win
        global b1, b2, b3, b4, b5, b6, b7, b8, b9

        gaming_window()
        count = 1
        win = 0
        b1, b2, b3, b4, b5, b6, b7, b8, b9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    if x==6:
        if scorex> score0:
            messagebox.showinfo("Winner of this game","player x is winner in this Game")
            res1=messagebox.askyesno("Give an another chanse to Looser!!!!!!!!!","Do you want to continue")
            print(res1)
            if res1:
                startNew()
        else:
            messagebox.showinfo("Winner of this game","Player 0 is winner")
            res1 = messagebox.askyesno("Give an another chanse to Looser!!!!!!!!!", "Do you want to continue")
            print(res1)
            if res1:
                startNew()



startNew()
root.title("Tic Tac Toe Game")
root.geometry("%dx%d+0+0"%(width,height))
root.mainloop()