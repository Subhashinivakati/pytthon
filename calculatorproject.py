
#calculator app
from tkinter import *


root=Tk()
root.title('Calculator App')


def btn_click(value):
    print(value)

def btn_click(value):
    global data
    data=data+str(value)

    input_text.set(data)

def btn_equal():
    global data
    result=str(eval(data))
    input_text.set(result)

def btn_clear():
    global data
    data=" "
    input_text.set(' ')


data=" "
input_text=StringVar()


input_frame=Frame(root,height=20,width=300,highlightbackground='black',highlightthickness=1)
input_frame.pack(side=TOP)

input_field=Entry(input_frame,width=22,textvariable=input_text,bg='#eee',justify=RIGHT,font=('times',20,'bold'))
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)

btn_frame=Frame(root,height=220,width=300,bg='lightgreen')
btn_frame.pack()

#first row

clear=Button(btn_frame,text='C',command=lambda:btn_clear(),bd=0,width=32,height=3).grid(row=0,column=0,columnspan=3,padx=1,pady=1)
devide=Button(btn_frame,text='/',command=lambda:btn_click('/'),bd=0,width=10,height=3).grid(row=0,column=3,padx=1,pady=1)

#second row

seven=Button(btn_frame,text=7,command=lambda:btn_click(7),bd=0,width=10,height=3).grid(row=1,column=0,padx=1,pady=1)
eight=Button(btn_frame,text=8,command=lambda:btn_click(8),bd=0,width=10,height=3).grid(row=1,column=1,padx=1,pady=1)
nine=Button(btn_frame,text=9,command=lambda:btn_click(9),bd=0,width=10,height=3).grid(row=1,column=2,padx=1,pady=1)
multiply=Button(btn_frame,command=lambda:btn_click(''),text='',width=10,height=3).grid(row=1,column=3,padx=1,pady=1)

#third row

six=Button(btn_frame,command=lambda:btn_click(6),text=6,bd=0,width=10,height=3).grid(row=2,column=0,padx=1,pady=1)
five=Button(btn_frame,command=lambda:btn_click(5),text=5,bd=0,width=10,height=3).grid(row=2,column=1,padx=1,pady=1)
four=Button(btn_frame,command=lambda:btn_click(4),text=4,bd=0,width=10,height=3).grid(row=2,column=2,padx=1,pady=1)
plus=Button(btn_frame,command=lambda:btn_click('+'),text='+',bd=0,width=10,height=3).grid(row=2,column=3,padx=1,pady=1)

#fourth row

three=Button(btn_frame,command=lambda:btn_click(3),text=3,bd=0,width=10,height=3).grid(row=3,column=0,padx=1,pady=1)
two=Button(btn_frame,command=lambda:btn_click(2),text=2,bd=0,width=10,height=3).grid(row=3,column=1,padx=1,pady=1)
one=Button(btn_frame,command=lambda:btn_click(1),text=1,bd=0,width=10,height=3).grid(row=3,column=2,padx=1,pady=1)
minus=Button(btn_frame,command=lambda:btn_click('-'),text='-',bd=0,width=10,height=3).grid(row=3,column=3,padx=1,pady=1)

#fifth row

zero=Button(btn_frame,command=lambda:btn_click(0),text=0,bd=0,width=22,height=3).grid(row=4,columnspan=2,padx=1,pady=1)
dot=Button(btn_frame,text='.',command=lambda:btn_click('.'),bd=0,width=10,height=3).grid(row=4,column=2,padx=1,pady=1)
equal=Button(btn_frame,text='=',command=lambda:btn_equal(),bd=0,width=10,height=3).grid(row=4,column=3,padx=1,pady=1)



root.mainloop()


