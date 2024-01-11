from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Calculator")

sty = ttk.Style()
sty.configure("TEntry",font =("Helvetica",20))

e = ttk.Entry(root,width = 35,font=("Helvetica", 10))
e.grid(row = 0,column = 0,columnspan = 4,padx = 12,pady = 10)

root.configure(bg='black')


def buttonAdd(num):
    current = str(e.get())
    e.delete(0,END)
    e.insert(0,current + str(num))
  
def buttonclear():
    e.delete(0,END)
def button_Add():
    first = e.get()
    global checker
    checker = 1
    global fnum
    fnum = float(first)
    e.delete(0,END)

def button_sub():
    first = e.get()
    global checker
    checker = 2
    global fnum
    fnum = float(first)
    e.delete(0,END)
    
def button_div():
    first = e.get()
    global checker
    checker = 3
    global fnum
    fnum = float(first)
    e.delete(0,END)
def button_mul():
    first = float(e.get())
    global checker
    checker = 4
    global fnum
    fnum = float(first)
    e.delete(0,END)
def intorfloat(num):
    check = str(num).split('.')
    part = check[1]
    for i in range(len(part)):
        if(part[i] !=0):
            return True
    return False
    
def buttonEqual():
    secondnum = float(e.get())
    e.delete(0,END)
    if(checker == 1):
        answer = fnum+secondnum
        if(intorfloat(answer)):
            e.insert(0,int(fnum)+int(secondnum))
        else:
            e.insert(0,fnum+secondnum)
    if(checker == 2):
        answer = fnum - secondnum
        if(intorfloat(answer)):
            e.insert(0,int(fnum)-int(secondnum))
        else:
            e.insert(0,fnum-secondnum)
    if(checker == 3):
        try:
            answer = fnum/secondnum
            
            if(intorfloat(answer)):
                answer = fnum//secondnum
                e.insert(0,int(answer))
            else:
                answer = fnum//secondnum
                e.insert(0,(answer))
        except Exception as ex:
                e.insert(0,ex)
        

    if(checker == 4):
        answer = fnum * secondnum
        if(intorfloat(answer)):
            e.insert(0,int(fnum)*int(secondnum))
        else:
            e.insert(0,fnum*secondnum)
    
button1 = Button(root,text = "1",padx = 40,pady = 40,command = lambda: buttonAdd(1))
button2 = Button(root,text = "2",padx = 40,pady = 40,command = lambda: buttonAdd(2))
button3 = Button(root,text = "3",padx = 40,pady = 40,command = lambda: buttonAdd(3))
button4 = Button(root,text = "4",padx = 40,pady = 40,command = lambda: buttonAdd(4))
button5 = Button(root,text = "5",padx = 40,pady = 40,command = lambda: buttonAdd(5))
button6 = Button(root,text = "6",padx = 40,pady = 40,command = lambda: buttonAdd(6))
button7 = Button(root,text = "7",padx = 40,pady = 40,command = lambda: buttonAdd(7))
button8 = Button(root,text = "8",padx = 40,pady = 40,command = lambda: buttonAdd(8))
button9 = Button(root,text = "9",padx = 40,pady = 40,command = lambda: buttonAdd(9))
button0 = Button(root,text = "0",padx = 40,pady = 40,command = lambda: buttonAdd(0))
buttonequal = Button(root,text = "=",padx = 87,pady = 40,command = buttonEqual)
buttonadd = Button(root,text = "+",padx = 39,pady = 40,command = button_Add)
button_clear = Button(root,text = "Clear",padx = 176,pady = 40,command = buttonclear)

buttonSub = Button(root,text = "-",padx = 40,pady = 40,command = button_sub)
buttonmul = Button(root,text = "x",padx = 39,pady = 40,command = button_mul)
buttondiv = Button(root,text = "/",padx = 40,pady = 40,command = button_div)
#put buttons on screen
button1.grid(row = 3,column = 0)
button2.grid(row = 3,column = 1)
button3.grid(row = 3,column = 2)
button4.grid(row =2 ,column = 0)
button5.grid(row = 2,column = 1)
button6.grid(row = 2,column =2 )
button7.grid(row =1 ,column =0 )
button8.grid(row = 1,column =1 )
button9.grid(row = 1,column =2 )
button0.grid(row =4 ,column = 0)

button_clear.grid(row = 5,column = 0,columnspan=5)
buttonadd.grid(row = 1,column = 4)
buttonequal.grid(row = 4,column =1,columnspan = 2)

buttonSub.grid(row = 2,column = 4)
buttondiv.grid(row = 3,column=4)
buttonmul.grid(row = 4,column = 4)

root.mainloop()
