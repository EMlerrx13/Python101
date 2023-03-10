from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import webbrowser


GUI = Tk() #หน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูลทั่วไป')
GUI.geometry('500x500') #ขนาดโปรแกรม

l1 = Label(GUI,text='โปรแกรมบันทึกข้อมูลทั่วไป',font=('Angsana New',30) , fg='#32a868')
l1.place(x=85,y=90)

def  btn1():
    text = 'kiratiziiz'
    messagebox.showinfo('ชื่อบัญชีผู้ใช้งาน : ',text)

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=60,y=150)
B1 = ttk.Button(FB1,text='ชื่อบัญชีผู้ใช้งาน', command=btn1)
B1.pack(ipadx=20,ipady=20)


def btn2():
    text = 'ตอนนี้มีเงินในบัญชี 75.08 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=300,y=150)
B2 = ttk.Button(FB2,text='มีเงินอยู่ในบัญชี', command=btn2)
B2.pack(ipadx=20,ipady=20)


def btn3():
    text = 'Python 101 - EP.2 \n-โมดูล/package/ไลบรารีคืออะไร?\n-built-in library\n-ตัวแปรเก็บข้อมูล\n-print แบบพิเศษ (.format)\n-basic tkinter สร้างโปรแกรมที่มีปุ่ม'
    messagebox.showinfo('สิ่งที่เรียนวันนี้',text)

FB3 = Frame(GUI) #คล้ายกระดาน
FB3.place(x=60,y=300)

B3 = ttk.Button(FB3,text='สิ่งที่เรียนวันนี้', command=btn3)
B3.pack(ipadx=20,ipady=20)


def btn4():
    link = "https://www.youtube.com/watch?v=4sj5bS2LVGQ"
    text = webbrowser.open(link)
    messagebox.showinfo('ทบทวนความรู้',text)

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=300,y=300)
B4 = ttk.Button(FB2,text='ทบทวนความรู้', command=btn4)
B4.pack(ipadx=20,ipady=20)


def btn5():
    text = 'ให้ออกแบบ GUI ตามที่เราต้องการ'
    messagebox.showwarning('การบ้าน',text)

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=180,y=420)
B5 = ttk.Button(FB2,text='การบ้าน', command=btn5)
B5.pack(ipadx=20,ipady=20)




GUI.mainloop()
