from tkinter import*
m = Tk(className="Checkbutton Demonstration")
m.geometry("300x200")
l = Label(m,text="Programming Languages",font = "50")
l.pack()
l1 = Label(m,text = 'You selected:   ',font = "50")
l2 = Label(m,text = '',font = "50")
checkbutton1=IntVar()
checkbutton2=IntVar()
checkbutton3=IntVar()

def check1():
    if checkbutton1.get():
        msg = "python"
        l2.config(text = msg)
    else:
        msg = "nothing"
        l2.config(text = msg)
def check2():
    if checkbutton2.get():
        msg = "java"
        l2.config(text = msg)
    else:
        msg = "nothing"
        l2.config(text = msg)
def check3():
    if checkbutton3.get():
        msg = "c programming"
        l2.config(text = msg)
    else:
        msg = "nothing"
        l2.config(text = msg)
def fun():
    w.config(text="Java is a ever green programming language")
CB1=Checkbutton(m,text="Python",
                                        variable= checkbutton1,
                                        onvalue=1,
                                        offvalue=0,
                                        height = 5,
                                        width=20, bg = "ORANGE",
                                        command = check1)
CB2=Checkbutton(m,text="Java",
                                        variable= checkbutton2,
                                        onvalue=1,
                                        offvalue=0,
                                        height = 5,
                                        width=20 ,bg = "SKY BLUE",
                                        command = check2)

CB3=Checkbutton(m,text="C Programming",
                                        variable= checkbutton3,
                                        onvalue=1,
                                        offvalue=0,
                                        height = 5,
                                        width=20 , bg = "BLUE",
                                        command = check3)
CB1.pack()
CB2.pack()
CB3.pack()
l1.pack()
l2.pack()
m.mainloop()

