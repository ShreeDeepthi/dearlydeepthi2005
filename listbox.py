from tkinter import*
from tkinter.messagebox import showinfo
root=Tk()
root.geometry("180x200")
listbox = Listbox(root,width=40,height=10,selectmode=MULTIPLE)
listbox.insert(1,"Data Structure")
listbox.insert(2,"Algorithms")
listbox.insert(3,"Data Science")
listbox.insert(4,"Machine Learning")
listbox.insert(5,"Block Chain")

def selected_item():
    for i in listbox.curselection():
        showinfo(title='POP UP Window',
                 message=f'You have selected a month:   (listbox.get(i))!')
        #print(listbox.get(i))
        
btn = Button(root,text = 'print selected',command = selected_item,activebackground="cyan")
btn.pack(side='bottom')
listbox.pack()
root.mainloop()
        
