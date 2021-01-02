from tkinter import*

root = Tk()
root.title("Woongstar GUI")
root.geometry("640x480")

text = Text(root, width=30, height=5)
text.pack()

text.insert(END, "글자를 입력하세요.")

e= Entry(root,width=30)
e.pack()
e.insert(0,"한줄만 입력해요.")

def btncmd():
    print(text.get("1.0",END))
    print(e.get())

    text.delete("1.0",END)
    e.delete(0,END)

btn = Button(root, text="click",command=btncmd)
btn.pack()
root.mainloop()
