import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Woongstar GUI")
root.geometry("640x480")

def info():
    msgbox.showinfo("Notice","정상적으로 예매가 완료되었습니다.")
def warn():
    msgbox.showwarning("Warning","해당 좌석은 매진되었습니다.")
def error():
    msgbox.showerror("Error","결제오류가 발생하였습니다.")
def okcancel():
    msgbox.askokcancel("확인/취소","다시 한번 확인해주세요")
def retrycancel():
    msgbox.askretrycancel("retry","다시 하번 도전해주세요.")
def yesno():
    msgbox.askyesno("yes/no","해당 좌석은 역방향입니다.")
def yesnocancel():
    response = msgbox.askyesnocancel(title=None,message="예매내역이 저장되지 않았습니다.")
    p
Button(root,command=info,text="Notice").pack()
Button(root,command=warn,text="Warning").pack()
Button(root,command=error,text="Error").pack()

Button(root,command=okcancel,text="cancel").pack()
Button(root,command=retrycancel,text="retry").pack()
Button(root,command=yesno,text="yes/no").pack()
Button(root,command=yesnocancel,text="yes/no/cancel").pack()

root.mainloop()
