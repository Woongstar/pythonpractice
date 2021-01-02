from tkinter import *

root = Tk()
root.title("Woongstar GUI")
root.geometry("640x480")

chkvar = IntVar()
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select()
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text= "일주일간 보지 않기",variable = chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get())
    print(chkvar2.get())


btn = Button(root, text="click",command=btncmd)
btn.pack()
root.mainloop()
