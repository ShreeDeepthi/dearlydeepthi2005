from tkinter import*
def selection():
    selection="You selected the option"+str(radio.get())
    Label.config(text=selection)
m = Tk()
m.geometry("300x150")
radio = IntVar()
lb1=Label(text = "Favourite Programming Language")
lb1.pack()
R1=Radiobutton(m,text="c",variable=radio,value=1,command=selection)
R1.pack(anchor=W)

R2=Radiobutton(m,text="python",variable=radio,value=2,command=selection)
R2.pack(anchor=W)

R3=Radiobutton(m,text="java",variable=radio,value=3,command=selection)
R3.pack(anchor=W)

Label=Label(m)
Label.pack()
m.mainloop()