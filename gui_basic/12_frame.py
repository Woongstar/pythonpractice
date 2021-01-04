import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Woongstar GUI")
root.geometry("640x480")
label1 = Label(root, text="Choose the menu").pack(side="top")
Button(root,text="Order").pack(side="bottom")
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left",fill="both",expand=True)

Button(frame_burger, text = "hamberger").pack()
Button(frame_burger, text = "Cheeze burger").pack()
Button(frame_burger, text = "Chicken burger").pack()

frame_drink = Frame(root, relief="solid",bd =1)
frame_drink.pack(side ="right",fill="both",expand=True)
Button(frame_drink,text="Coke").pack()
Button(frame_drink,text="Sprite").pack()


root.mainloop()
