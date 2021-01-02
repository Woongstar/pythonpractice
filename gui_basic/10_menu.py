from tkinter import *

root = Tk()
root.title("Woongstar GUI")
root.geometry("640x480")

menu = Menu(root)

def create_new_file():
    print("create new file")

menu_file = Menu(menu,tearoff=0)
menu_file.add_command(label="New File",command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All",state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit",command = root.quit)

menu.add_cascade(label="Edit")
menu.add_cascade(label="File",menu=menu_file)

menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language",menu=menu_lang)

menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="view",menu=menu_view)

root.config(menu=menu)
root.mainloop()
