from tkinter import *

m = Tk()
m.geometry("450x300")
m.title("User Interface")

attempts = 3  

def take_details():
    global attempts
    user_name = t1.get()
    password = t2.get()
    
    if user_name == "deepthi" and password == "2005":
        status_label.config(text="Your credentials are correct ")
    else:
        attempts -= 1
        if attempts > 0:
            status_label.config(text=f"Your credentials are wrong, you have {attempts} more chance(s)")
        else:
            status_label.config(text="Your credentials are wrong, your account is blocked")
            b1.config(state=DISABLED)  

# The label for user name
l1 = Label(m, text="USER_NAME")
# The label for user_password
l2 = Label(m, text="PASSWORD")
t1 = Entry(m, width=30)
t2 = Entry(m, width=30)
b1 = Button(m, text="Submit", command=take_details, activebackground="red")
status_label = Label(m, text="", fg="black")

l1.place(x=40, y=60)
t1.place(x=110, y=60)
l2.place(x=40, y=100)
t2.place(x=110, y=100)
b1.place(x=40, y=130)
status_label.place(x=40, y=160)

m.mainloop()