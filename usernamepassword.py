from tkinter import *
m = Tk() 
m.geometry("450x300") 
m.title("User Interface")
username_var=StringVar()
passw_var=StringVar()
def submit():
    username = username_var.get()
    password = passw_var.get()
    if username=="deepthi@gmail.com" and password =="2005":
        print("successful validation")
    else:
        print("invalid credentials two more attempts left ")
        if username=="deepthi@gmail.com" and password =="2005":
            print ("successful validation")
        else:
            print("invalid credentials one more attempt left ")
            else:
                print("try again later")
    print("the name is :"+username)
    print("the password is:"+password)
    username_var.set("")
    passw_var.set("")
# the label for user_name 
l1 = Label(m, text = "Username")
# the label for user_password 
l2 = Label(m, text = "Password")
t1 = Entry(m,width = 30, textvariable = username_var)
t2 = Entry(m, width = 30, textvariable = passw_var, show = "*")
b1 = Button(m, text = "Submit", command = submit)
l1.place(x = 40,y=60)
t1.place(x = 110,y = 60)
l2.place(x = 40,y=100)
t2.place(x = 110, y=100)
b1.place(x = 40,y=130)

m.mainloop()