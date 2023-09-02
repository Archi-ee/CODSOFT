# Creating a simple calculator using python and tkinter library
from tkinter import *
root=Tk()
root.title("Calculator")
root.geometry("350x578")
root.resizable(0,0)


p1 = PhotoImage(file = r"C:\Users\ARCHI JAIN\PycharmProjects\mysmallProject\codsoftinternship\cal5.png")
root.iconphoto(False,p1)

def click(event):
    global strvalue
    text=event.widget.cget("text")
    if text=="=":
        if strvalue.get().isdigit():
            value= int(strvalue.get())
        else:
            try:
                value=eval(screen.get()) 
            except Exception as e:
                print(e)
                value="Error"
        strvalue.set(value)
        screen.update()
    elif text=="C":
        strvalue.set("")
        screen.update()
    else:
        strvalue.set(strvalue.get()+text)
        screen.update()

strvalue=StringVar()
strvalue.set("")

input_frame=Frame(root,width=312,height=324 ,highlightthickness=2)
input_frame.pack()

screen=Entry(input_frame,font=("lucide",40,"bold"),textvariable=strvalue,width=50,bg="lightblue",justify="right")
screen.grid(row=0,column=0)
screen.pack(ipady=10)

button_frame=Frame(root,width=350,height=450,bg="grey")
button_frame.pack()
# creating buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+ ", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("- ", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("* ", 3, 3),
    ("00", 4, 0), ("0", 4, 1), (".", 4, 2), ("/", 4, 3),
    ("%",5,2)
    ]


for button_text, row, column in buttons:
    button = Button(button_frame, text=button_text, width=4,height=2, padx=5,pady=5 ,cursor="hand2",font="lucide 20 bold")
    button.grid(row=row, column=column)
    button.bind("<Button-1>",click)

button1=Button(button_frame, text="C",bg="gray", width=9, height=2, padx=5, pady=5,cursor="hand2",font="lucide 20 bold")
button1.grid(row=5,column=0,columnspan = 2)
button1.bind("<Button-1>",click)

button1=Button(button_frame, text="=",bg="gray", width=4, height=2, padx=5, pady=5,cursor="hand2",font="lucide 20 bold")
button1.grid(row=5,column=3)
button1.bind("<Button-1>",click)

root.mainloop()
