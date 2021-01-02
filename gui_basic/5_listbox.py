from tkinter import *

root = Tk()
root.title("Woongstar GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0,"사과")
listbox.insert(1,"포도")
listbox.insert(2,"귤")
listbox.insert(END,"수박")
listbox.insert(END,"바나나")
listbox.pack()

def btncmd():
    #delete
    # listbox.delete(0)
    #check size
    # print("There are",listbox.size(),"components in the listbox")
    #chech index
    # print("from 1 to third",listbox.get(0,2))
    #check selected components
    print("selected components",listbox.curselection())
btn = Button(root, text="click",command=btncmd)
btn.pack()
root.mainloop()
