from tkinter import *
import math
def left_at_button(event):
    height = float(textbox1.get())
    weight = float(textbox2.get())
    BMI = weight/(height**2)
    if BMI <18.5:
        x = 'ผอมเกินไป'
    elif math.floor(BMI) <23.0:
        x = 'น้ำหนักปกติ'
    elif math.floor(BMI) < 25.0:
        x = 'น้ำหนักเกิน'
    elif math.floor(BMI) < 30.0:
        x = 'อ้วน'
    else:
        x = 'อ้วนมาก'
    labal4.configure(text='คุณอยู่ในเกณฑ์ %s'%x)
    chainwin =Tk()
    labal3 = Label(chainwin, text='Your BMI is %.2f'%BMI)
    labal3.pack()
mainwin = Tk()
labal1 = Label(mainwin,text='ส่วนสูง(m)',width=30).grid(row=1,column=0)
labal2 = Label(mainwin,text='น้ำหนัก(kg)',width=30).grid(row=2,column=0)
textbox1 = Entry(mainwin,width=50)
textbox1.grid(row=1,column=1)
textbox2 = Entry(mainwin,width=50)
textbox2.grid(row=2,column=1)
button1 = Button(mainwin,text='คำนวนBMI',height=5,width=20)
button1.bind('<Button-1>',left_at_button)
button1.grid(row=3,column=0)
labal4 = Label(mainwin,text='ผลลัพธ์')
labal4.grid(row=3,column=1)
button1.bind()
mainwin.mainloop()