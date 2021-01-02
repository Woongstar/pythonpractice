from tkinter import *

root = Tk()
root.title("Woongstar GUI")
root.geometry("640x480")

label1 = Label(root, text="메뉴를 입력하세요").pack()

radio_var = IntVar()
radiobtn1 = Radiobutton(root, text="Hamburger",value=1,variable=radio_var)
radiobtn1.select()
radiobtn2 = Radiobutton(root, text="Cheeze Hamburger",value=2,variable=radio_var)
radiobtn3 = Radiobutton(root, text="Chicken Hamburger",value=3,variable=radio_var)

radiobtn1.pack()
radiobtn2.pack()
radiobtn3.pack()

label2 = Label(root,text="음료를 선택하세요").pack()

drink_var = StringVar()

btn_drink1 = Radiobutton(root,text="Coke",value="Cock",variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root,text="Sprite",value="Sprite",variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(radio_var.get())
    print(drink_var.get())
btn = Button(root, text="click",command=btncmd)
btn.pack()
root.mainloop()
