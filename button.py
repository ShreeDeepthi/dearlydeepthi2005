import tkinter as tk
#from tkinter import*
#from tkinter.ttk import*
m=tk.Tk()
m.title("Button Demonstration")
m.geometry("200x200")
b1=tk.Button(m,text = "STOP")#,width = 20,height = 2,bd = 5,font = 20,command=m.destroy,activebackground="blue")
b2=tk.Button(m,text = "Submit")#,width = 20,height = 2,bd = 5,font = 20,command=m.destroy,activebackground="blue")
b3=tk.Button(m,text = "Clear")#,width = 20,height = 2,bd = 5,font = 20,command=m.destroy,activebackground="blue")
b4=tk.Button(m,text="Nothing")
'''b1.pack(side='left')
b2.pack(side='right')
b3.pack(side='top')'''
b1.grid(row=0,column=0,pady=2)
b2.grid(row=0,column=1,pady=2)
b3.grid(row=0,column=2,pady=2)
b4.grid(row=0,column=3,pady=2)
'''b1=Button(m,text="Click me!")
b1.place(relx=1,x=2,y=2,anchor = CENTER)'''
m.mainloop()


