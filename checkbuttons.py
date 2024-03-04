from tkinter import*
m = Tk(className="Checkbutton Demonstration")
m.geometry("300x200")
w = Label(m,text="Programming Languages",font = "50")
w.pack()
Checkbutton1=IntVar()
Checkbutton2=IntVar()
Checkbutton3=IntVar()
def fun():
    w.config(text="Java is a ever green programming language")
CB1=Checkbutton(m,text="Python",
                                        variable= Checkbutton1,
                                        onvalue=1,
                                        offvalue=0,
                                        height = 5,
                                        width=20)
CB2=Checkbutton(m,text="Java",
                                        variable= Checkbutton2,
                                        onvalue=1,
                                        offvalue=0,
                                        height = 5,
                                        width=20,
                                        activebackground="RED",command=fun)

CB3=Checkbutton(m,text="C Programming",
                                        variable= Checkbutton3,
                                        onvalue=1,
                                        offvalue=0,
                                        height = 5,
                                        width=20,bg="BLUE")
def check1():
    if Checkbutton1.get():
        msg = "Python"
        m.config(text = msg)
    else:
        msg = "Nothing"
        m.config(text = msg)
def check2():
    if Checkbutton2.get():
        msg = "Java"
        m.config(text = msg)
    else:
        msg = "Nothing"
        m.config(text = msg)
def check3():
    if Checkbutton3.get():
        msg = "C Programming"
        m.config(text = msg)
    else:
        msg = "Nothing"
        m.config(text = msg)
CB1.pack()
CB2.pack()
CB3.pack()
m.mainloop()
