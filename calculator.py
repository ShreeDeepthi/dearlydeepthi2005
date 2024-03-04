import tkinter as tk

def perform_operation(operation):
    try:
        value1 = float(entry1.get())
        value2 = float(entry2.get())

        if operation == "Addition":
            result = value1 + value2
        elif operation == "Multiplication":
            result = value1 * value2
        elif operation == "Division":
            result = value1 / value2
        elif operation == "Subtraction":
            result = value1 - value2
        else:
            result = "Invalid Operation"

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

def clear_entries():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result:")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widgets for user input
entry1_label = tk.Label(root, text="Enter Value 1:")
entry1_label.grid(row=0, column=0, padx=10, pady=10, sticky="E")
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

entry2_label = tk.Label(root, text="Enter Value 2:")
entry2_label.grid(row=1, column=0, padx=10, pady=10, sticky="E")
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Label to display the result
result_label = tk.Label(root, text="Result:")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Buttons for operations and clear
operations = ["Addition", "Multiplication", "Division", "Subtraction"]
for i, operation in enumerate(operations):
    button = tk.Button(root, text=operation, command=lambda op=operation: perform_operation(op))
    button.grid(row=3, column=i, padx=10, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_entries)
clear_button.grid(row=4, column=0, columnspan=4, pady=10)

# Start the main loop
root.mainloop()

