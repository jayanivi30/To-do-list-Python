import tkinter as tk
from sys import excepthook
from tkinter import messagebox

#function to load tasks
def load_tasks():
     try:
         with open("tasks.txt","r") as file:
             tasks = file.readlines()
             for task in tasks:
                 listbox.insert(tk.END,task.strip())
     except FileNotFoundError:
         pass

#function to save tasks
def save_tasks():
    tasks = listbox.get(0,tk.END)
    with open("tasks.txt","w") as file:
        for task in tasks:
            file.write(task + "\n")


#function to add task
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END,task)
        entry.delete(0,tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error","Please enter a task.")

#function to delete task
def del_task():
    try:
        selected_task_index = listbox.curselection()
        listbox.delete(selected_task_index)
        save_tasks()
    except:
        messagebox.showwarning("Selection error","Please select a task to delete")

#creating a window
root = tk.Tk()
#title
root.title("To-do-app")
#geometry
root.geometry("400x400")

#listbox widget to display the tasks
listbox = tk.Listbox(root,width=40,height=10)
listbox.pack(pady=10)

#load tasks
load_tasks()

#entry widget
entry = tk.Entry(root,width=40)
entry.pack(pady=10)

#adding an add_button
add_button = tk.Button(root,text="Add Task",width=20,command=add_task)
add_button.pack(pady=10)

#adding a del_button
del_button = tk.Button(root,text="Delete task",width=20,command=del_task)
del_button.pack(pady=10)

#to keep the window running
root.mainloop()
