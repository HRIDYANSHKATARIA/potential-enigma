from tkinter import *

root = Tk()

root.title("Grades")
root.geometry("400x400")

def btn1f():
    lab1(root,text="45%",fg="red")
    
def btn2f():
    lab2(root,text="60%",fg="red")
    
def btn3f():
    lab3 = Label(root,text="62.5%",fg="red")
    
btn1 = Button(root,text="Grade 3",command=btn1f)
btn1.place(relx=0.5,rely=0.2)

lab1 = Label(root,text="",fg="red")
lab1.place(relx=0.5,rely=0.3)

btn2 = Button(root,text="Grade 5",command=btn2f)
btn2.place(relx=0.5,rely=0.5)

lab2 = Label(root,text="",fg="red")
lab2.place(relx=0.5,rely=0.6)

btn3 = Button(root,text="Grade 10",command=btn3f)
btn3.place(relx=0.5,rely=0.8)

lab3 = Label(root,text="",fg="red")
lab3.place(relx=0.5,rely=0.9)

root.mainloop()
