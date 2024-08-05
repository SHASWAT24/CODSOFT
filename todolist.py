from tkinter import *

win = Tk()
win.title("TO Do LIST")
win.geometry("300x550+700+100")
win.resizable(False, False)

def openTaskFile():
    try:
        global task_lists
        with open("taskfile.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task:  
                task_lists.append(task)
                box.insert(END, task)
    except FileNotFoundError:
        with open("taskfile.txt", "w"):
            pass

def addTask():
    task = task_enter.get()
    task_enter.delete(0, END)
    if task:
        with open("taskfile.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_lists.append(task)
        box.insert(END, task)


def deleteTask():
    global task_lists
    task = str(box.get(ANCHOR))
    if task in task_lists:
        task_lists.remove(task)
        with open("taskfile.txt", "w") as taskfile:
            for task in task_lists:
                taskfile.write(task + "\n")
        box.delete(ANCHOR)

# GUI Layout
heading = Frame(win, width=400, height=50, bg="black")
heading.pack()

Label(win, text="ADD TASK", font=("arial bold", 20), bg="black", fg="white").place(x=75, y=5)

frame = Frame(win, width=300, height=48, bg="white")
frame.place(x=0, y=100)
task_enter = Entry(frame, width=18, font="arial 20", bd=0)
task_enter.place(x=10, y=7)
task_enter.focus()

Button(frame, text="Add", font="arial 20 bold", width=6, bg="black", fg="white", bd=0, command=addTask).place(x=200, y=0)

lb = Frame(win, bd=3, width=700, height=280, bg="black")
lb.pack(pady=(100, 0))
box = Listbox(lb, font=("arial", 12), width=40, height=16, bg="black", fg="white", cursor="hand2", selectbackground="white")
scroll = Scrollbar(lb)
box.config(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=BOTH)
box.pack(side=LEFT, fill=BOTH, padx=2)

Button(win, text="Delete", font=("Arial bold", 15), width=6, bg="black", fg="white", command=deleteTask).pack(pady=(15, 0))


task_lists = []
openTaskFile()

win.mainloop()