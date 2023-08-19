 #random and secure password generator GUI in tkinter 

from tkinter import *

from tkinter import messagebox

from tkinter import Image

import string

import random

root = Tk()

root.resizable(False,False)

root.config(bg="white")

root.geometry("750x400+400+150")



root.iconbitmap("logo.ico")



def number():

    try:

        int(number_entry.get())

    

        s1 = string.ascii_lowercase

        s2 = string.ascii_uppercase

        s3 = string.digits

        s4 = string.punctuation



        #plen = password lenght

        plen = int(number_entry.get())

        s = []

        s.extend(list(s1))

        s.extend(list(s2))

        s.extend(list(s3))

        s.extend(list(s4))



        random.shuffle(s)



        a = ("".join(s[0:plen]))



        # print(a)

        passwords_in_screen.insert(0, a)

        passwords_in_screen.config(state="readonly")

        

    

    except ValueError:

        messagebox.showerror("error","Pls Enter Number")



root.title(" Password Generator ||  By Aarohi Pisolkar")

title = Label(text="Secure Your Accounts using Strong Password",compound=LEFT, bg="#222A35",fg="white", font=("Fixedsys", 20, "bold"))

title.pack()



# entery field of number (password lenght input field)

number_entry = Entry(root, font=("times new roman", 14),bg="white")

number_entry.place(x=3, y=130,width=450, height=30)



# telling user for input number of lenght label



Input_label = Label(text="Enter the Lenght of Your Password ↓",compound=LEFT,bg="lightgreen",fg="black", font=("times new roman", 22, "italic", "bold")).place(y=70)



# Lock Image

photo = PhotoImage(file="pass.png")

ph_label = Label(image=photo, bg="white") 

ph_label.place(x=490, y=70)



#button

bt = Button(root,text="Generate Password", bd=1,command=number,font=("times new roman", 18, "bold", "italic"), bg="lightgreen", activebackground="#00B0F0",activeforegroun="white", fg="black", cursor="hand2")

bt.place(x=100, y=190)





#(label) for desiging and good look

bottom_title = Label(text="Security Comes First! || By Aarohi Pisolkar",bg="lightgreen", fg="black",font=("Calibri (bold)", 25))

bottom_title.pack(side=BOTTOM)



passwords_in_screen = Entry(root, font=("times new roman", 14),bd=0)

passwords_in_screen.place(x=3, y=270,width=450, height=30)


# new_bt = Button(text="wan to secure excisting ")

root.mainloop()

#By Aarohi Pisolkar

