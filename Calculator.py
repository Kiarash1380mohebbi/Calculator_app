from customtkinter import *
from tkinter import *

win = CTk()
win.title('Calculator')
win.geometry('308x190+520+200')
win.attributes(topmost=TRUE)
win._set_appearance_mode('light')
win.resizable(False,False)

equations = ""

def show(value):
    global equations
    equations += value
    equation.delete(0, END)
    equation.insert(0, equations)

def clear():
    global equations
    equations = ""
    equation.delete(0, END)

def delete():
    global equations
    equations = equations[:-1]
    equation.delete(0, END)
    equation.insert(0, equations)

def calculate():
    global equations
    result = ""
    if equations != "":
        try:
            expr = equations.replace('x', '*').replace('%', '/')
            result = str(eval(expr))
        except:
            result = "Error!"
        equations = result
    equation.delete(0, END)
    equation.insert(0, result)


equation = CTkEntry(win, width=300, height=50, placeholder_text='0',
                    placeholder_text_color="#727070", fg_color="#C9DAD9",
                    font=('Arial', 20), text_color="#1B1919", justify='right')
equation.grid(row=0, columnspan=4, padx=1, pady=5)


#دکمه ها
#Buttons
#row 1
btn_1=CTkButton(win,text='1',text_color="#000000",fg_color="#42A8C2",width=75,command=lambda:show("1"))
btn_2=CTkButton(win,text='2',text_color="#000000",fg_color="#42A8C2",width=75,command=lambda:show("2"))
btn_3=CTkButton(win,text='3',text_color="#000000",fg_color="#42A8C2",width=75,command=lambda:show("3"))
btn_Positive=CTkButton(win,text='+',text_color="#FFFFFF",fg_color="#FF5100",width=75,command=lambda:show("+"))
#row 2
btn_4=CTkButton(win,text='4',text_color="#000000",fg_color="#42A8C2",width=75,command=lambda:show("4"))
btn_5=CTkButton(win,text='5',text_color="#000000",fg_color="#42A8C2",width=75,command=lambda:show("5"))
btn_6=CTkButton(win,text='6',text_color="#000000",fg_color="#42A8C2",width=75,command=lambda:show("6"))
btn_Negative=CTkButton(win,text='-',text_color='#ffffff',fg_color="#FF5100",width=75,command=lambda:show("-"))
#row 3
btn_7=CTkButton(win,text='7',text_color="#000000",fg_color="#42A8C2",width=75,command=lambda:show("7"))
btn_8=CTkButton(win,text='8',text_color="#000000",fg_color="#42A8C2",width=75,command=lambda:show("8"))
btn_9=CTkButton(win,text='9',text_color="#000000",fg_color="#42A8C2",width=75,command=lambda:show("9"))
btn_Multiplication=CTkButton(win,text='x',text_color='#ffffff',fg_color="#FF5100",width=75,command=lambda:show("x"))
#row 4
btn_equal=CTkButton(win,text='=',text_color='#ffffff',fg_color="#FF5100",width=75,command=calculate)
btn_0=CTkButton(win,text='0',text_color="#000000",fg_color="#42A8C2",width=75,command=lambda:show("0"))
btn_Delete=CTkButton(win,text='D',text_color='#ffffff',fg_color="#C00000",width=75,command=clear)
btn_Division=CTkButton(win,text='%',text_color='#ffffff',fg_color="#FF5100",width=75,command=lambda:show("/"))

#Button settings on the window
btn_1.grid_configure(row=1,column=0,padx=1,pady=2)
btn_2.grid_configure(row=1,column=1,padx=1,pady=2)
btn_3.grid_configure(row=1,column=2,padx=1,pady=2)
btn_Positive.grid_configure(row=1,column=3,padx=1,pady=2)
btn_4.grid_configure(row=2,column=0,padx=1,pady=2)
btn_5.grid_configure(row=2,column=1,padx=1,pady=2)
btn_6.grid_configure(row=2,column=2,padx=1,pady=2)
btn_Negative.grid_configure(row=2,column=3,padx=1,pady=2)
btn_7.grid_configure(row=3,column=0,padx=1,pady=2)
btn_8.grid_configure(row=3,column=1,padx=1,pady=2)
btn_9.grid_configure(row=3,column=2,padx=1,pady=2)
btn_Multiplication.grid_configure(row=3,column=3,padx=1,pady=2)
btn_equal.grid_configure(row=4,column=2,padx=1,pady=2)
btn_0.grid_configure(row=4,column=1,padx=1,pady=2)
btn_Delete.grid_configure(row=4,column=0,padx=1,pady=2)
btn_Division.grid_configure(row=4,column=3,padx=1,pady=2)


win.mainloop()