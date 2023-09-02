import tkinter
from tkinter import *
from tkinter.simpledialog import askstring
root=Tk()
root.title("To-Do-List")
root.geometry("400x450")
root.resizable(0,0)
list_frame=Frame(root)
root.config(bg="light blue") 

p2 = PhotoImage(file ="mysmallProject/codsoftinternship/icop.png")
root.iconphoto(False,p2)


def task():
    task_value = askstring("Task", "Write your task")
    if task_value:
        task_list.insert(END, task_value)

def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)

def done_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)
    task_list.insert(selected_task, "Task Completed")


def delete_all_tasks():
    task_list.delete(0, END)
imagee=PhotoImage(file="mysmallProject/codsoftinternship/TO-DO-LIST (1).png")
l=Label(root,image=imagee,width='400',height="175")
l.pack()

button_frame=Frame(root,height="300",width="400")
button_frame.pack()
button_frame.config(bg="light blue")


plus_image=PhotoImage(file="mysmallProject/codsoftinternship/resize-1693141514743468920downloadremovebgpreview-removebg-preview.png",width=50,height=50)
plus_label=Label(image=plus_image)


button1=Button(button_frame, image=plus_image ,command=task)
button1.place(x=20,y=200)

del_image=PhotoImage(file="mysmallProject/codsoftinternship/resize-16931424691281822332delete.png")
del_label=Label(image=del_image)

del_button=Button(button_frame, image=del_image,command=remove_task)
del_button.place(x=100,y=200)

tick_image=PhotoImage(file="mysmallProject/codsoftinternship/resize-1693168318197023422tick.png")
tick_label=Label(image=tick_image)

tick_button=Button(button_frame, image=tick_image, command=done_task)
tick_button.place(x=180,y=200)

delete_all_tasks=Button(button_frame, text="delete all",command=delete_all_tasks)
delete_all_tasks.place(x=310,y=220)

task_list=Listbox(button_frame,width=60,height=10)
task_list.place(x=0,y=0)

scrollbar = Scrollbar(button_frame, orient=VERTICAL, command=task_list.yview)
scrollbar.place(x=380, y=0, height=180)
task_list.config(yscrollcommand=scrollbar.set)

root.mainloop()