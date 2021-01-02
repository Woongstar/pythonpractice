import tkinter.ttk as ttk
from tkinter import *
import time
root = Tk()
root.title("Woongstar GUI")
root.geometry("640x480")

# progressbar = ttk.Progressbar(root,maximum=100,mode="indeterminate")
# progressbar = ttk.Progressbar(root,maximum=100,mode="determinate")
# progressbar.start(10)#10ms마다 움직임
# progressbar.pack()
#
# def btncmd():
#     progressbar.stop()
#
# btn = Button(root, text="click",command=btncmd)
# btn.pack()
p_var2=DoubleVar()
progressbar2 = ttk.Progressbar(root,maximum=100,length=150,variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(0,101):
        time.sleep(0.01)

        p_var2.set(i)
        progressbar2.update()
        print(p_var2.get(),"%")


btn = Button(root, text="click",command=btncmd2)
btn.pack()

root.mainloop()
