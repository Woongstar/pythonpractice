from tkinter import*

root = Tk()
root.title("Woongstar GUI")

root.geometry("640x480")

label1 = Label(root,text="Hi there")
label1.pack()

photo = PhotoImage(file="gui_button.png")
label2 = Label(root,image=photo)
label2.pack()

def change():
    label1.config(text="클릭했어요")

    global photo2
    photo2 = PhotoImage(file="x_button.png")
    label2.config(image = photo2)

btn1 = Button(root,text="클릭해주세요",command = change)
btn1.pack()

root.mainloop()
