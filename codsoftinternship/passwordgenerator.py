import tkinter
from tkinter import *
import random
import string
from tkinter import messagebox
root=Tk()
root.title("Password Generator")
root.geometry("350x450")
root.resizable(0,0)
list_frame=Frame(root)
root.config(bg="#856ff8")

p2 = PhotoImage(file ="mysmallProject/codsoftinternship/passwo.png")
root.iconphoto(False,p2)

entry_var=IntVar()
password_var=IntVar()
password_type = StringVar()

def clicked():
        num=entry_var.get()
        
        upper_char="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower_char="abcdefghijklmnopqrstuvwxyz"
        digit="1234567890"
        symbol="!#$%&'()~`{}()+-*>?.<,/\|[]=:;"
        if num==0:
                messagebox.showinfo("ERROR","Enter valid digit")
                password_var.set(" ")
        elif num<=5:
                messagebox.showinfo("ERROR","Enter digit greater than 5")
                password_var.set(" ")
        else:
                if password_type.get() == "Easy":
                        characters = upper_char + lower_char + digit
                else:
                        characters = upper_char + lower_char + digit + symbol
                password = ''.join(random.choice(characters) for _ in range(num))
                password_var.set(password)

def use():
        text_to_copy = password1.get()
        root.clipboard_append(text_to_copy) 
        root.update() 



def make_readonly(text_widget):
        text_widget.config(state=DISABLED)  

T = Text(root,bg="grey",font="Calibri", height = 3, width = 70)
text1="""               Do you think your password 
                    will get hacked easily ?
                            try me ^^"""
T.pack()
T.insert(END,text1)


number_ques = Text(root,bg="white",font="Calibri", height = 2, width = 70)
text3="""                Enter the number of digits of
                         password you want"""

number_ques.place(x=0,y=100)
number_ques.insert(END,text3)



entry1=Entry(root,bg="light grey",font="Calibri",  width =20,textvariable=entry_var)
entry1.place(x=30,y=170)


button1=Button(root,bg="grey",font="Calibri",text="Enter",command=clicked)
button1.place(x=270,y=160)

easy_radio = Radiobutton(root, text="Easy", variable=password_type, value="Easy")
easy_radio.place(x=30, y=200)

complex_radio = Radiobutton(root, text="Complex", variable=password_type, value="Complex")
complex_radio.place(x=100, y=200)

T2=Text(root,bg= "white",font="Calibri", height = 1, width =50)
text2="""Your required password is ^^ """
T2.place(x=0,y=250)
T2.insert(END,text2)

make_readonly(T)
make_readonly(T2)
make_readonly(number_ques)


password1=Entry(root,bg="light grey",font="Calibri",width=30,textvariable=password_var)
password1.place(x=30,y=300)
password1.config(state=DISABLED)

regenerate_button=Button(root,bg="grey",font="Calibri",text="Regenerate",command=clicked)
regenerate_button.place(x=30,y=340)
use_button=Button(root,bg="grey",font="Calibri",text="Use",command=use)
use_button.place(x=270,y=340)


root.mainloop()

