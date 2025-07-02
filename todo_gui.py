import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

# Function to delete selected task
def delete_task():
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Create main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("300x400")

# Title label
tk.Label(root, text="📝 To-Do List", font=("Helvetica", 16)).pack(pady=10)

# Entry for new task
entry = tk.Entry(root, width=25)
entry.pack(pady=10)

# Buttons
tk.Button(root, text="Add Task", width=20, command=add_task).pack(pady=5)
tk.Button(root, text="Delete Task", width=20, command=delete_task).pack(pady=5)

# Listbox to show tasks
listbox = tk.Listbox(root, width=30, height=10)
listbox.pack(pady=10)

# Start the GUI loop
root.mainloop()
