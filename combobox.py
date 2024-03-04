import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name
root = tk.Tk()
#configure the root window
root.geometry("300x200")
root.title("Combobox Widget")
#label
Label = ttk.Label(text="please select the month")
Label.pack(fill=tk.X,padx=5,pady=5)
selected_month = tk.StringVar()
#create a combo box
month_cb = ttk.Combobox(root,textvariable=selected_month)
month_cb['values'] == [month_name[m][0:3] for m in range (1,13)]
month_cb['state'] = 'readonly'
#place the widget
month_cb.pack(fill=tk.X,padx=5,pady=5)
#bind the selected value changes
def month_changed(event):
    showinfo(
        title = "pop up window",
        message = f"You have selected a month : (selected_month.get())!")
month_cb.bind("<<ComboboxSelected>>",month_changed)
root.mainloop()
    