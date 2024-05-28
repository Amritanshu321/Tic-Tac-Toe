from  tkinter import *
root =Tk()
def something():
    my_button.config(text="you have been configged",fg="yellow")
    root.config(bg="blue")
global my_button
my_button=Button(root,text="click me",command=something)
my_button.pack()
root.geometry("500x500+100+100")
root.mainloop()