from tkinter import *
import math
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

root = Tk()
root.title('Calculator')
root.geometry('185x300')
root.resizable(0,0)

operator = StringVar()
n1 = StringVar()
n2 = StringVar()
turn = 1
equaled = True


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' math methods '''

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def divi(n1, n2):
    if n2 == 0:
        return 0
    else:
        return n1 / n2

def power(n1,n2):
    return n1 ** n2

def sqr_root(n1):
    return math.sqrt(n1)

def thr_root(n1):
    return math.pow(n1, (1/3))

def equal():
    global equaled
    global turn
    output = 0
    if operator != '' and n1.get() != '' and n2.get() != '':
        if operator.get() == '+':
            output = add(float(n1.get()),float(n2.get()))
            turn = 1
        elif operator.get() == '-':
            output = sub(float(n1.get()),float(n2.get()))
            turn = 1
        elif operator.get() == '*':
            output = mult(float(n1.get()),float(n2.get()))
            turn = 1
        elif operator.get() == '/':
            output = divi(float(n1.get()),float(n2.get()))
            turn = 1
        elif operator.get() == '**':
            output = power(float(n1.get()),float(n2.get()))
            turn = 1
    else:
        output = 0
        turn = 1
    #print('n1 is: ' + str(n1.get()))                       Debugging
    #print('n2 is: ' + str(n2.get()))                       Debugging
    ent.set(str(output))
    n1.set(''),n2.set(''),operator.set('')
    equaled = False
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' operator methods '''

def plus():
    operator.set('+')
    global turn 
    turn +=1
    ent.set('')

def minus():
    operator.set('-')
    global turn 
    turn +=1
    ent.set('')

def times():
    operator.set('*')
    global turn 
    turn +=1
    ent.set('')

def divide():
    operator.set('/')
    global turn 
    turn +=1
    ent.set('')

def power_set():
    operator.set('**')
    global turn 
    turn +=1
    ent.set('')

def square_root():
    if turn % 2 == 0:
        if n2.get() == '':
            if ent.get() == '' or 'ERROR':
                output = 'ERROR' 
            else:
                output = sqr_root(float(ent.get()))
        else:
            output = sqr_root(float(n2.get()))
            n2.set(output)
    else:
        if n1.get() == '':
            if ent.get() == '' or 'ERROR':
                output = 'ERROR' 
            else:
                output = sqr_root(float(ent.get()))
        else:
            output = sqr_root(float(n1.get()))
            n1.set(output)
    ent.set(str(output))

def root3():
    if turn % 2 == 0:
        if n2.get() == '':
            if ent.get() == '' or 'ERROR':
                output = 'ERROR' 
            else:
                output = thr_root(float(ent.get()))
        else:
            output = thr_root(float(n2.get()))
            n2.set(output)
    else:
        if n1.get() == '':
            if ent.get() == '' or 'ERROR':
                output = 'ERROR' 
            else:
                output = thr_root(float(ent.get()))
        else:
            output = thr_root(float(n1.get()))
            n1.set(output)
    ent.set(str(output))

def clear():
    if turn % 2 == 0:
        n2.set('')
        ent.set('')
    else:
        n1.set('')
        ent.set('')

def clear_all():
    global turn 
    turn = 1
    n1.set('')
    n2.set('')
    ent.set('')

def back():
    temp = ''
    if turn % 2 == 0:
        temp = str(n2.get())
        temp = temp[0:len(temp)-1]
        n2.set(temp)
        ent.set(temp)
    else:
        temp = str(n1.get())
        temp = temp[0:len(temp)-1]
        n1.set(temp)
        ent.set(temp)

def rec():
    if turn % 2 == 0:
        if n2.get() == '':
            if ent.get() == '' or 'ERROR':
                output = 'ERROR' 
            else:
                output = divi(1,float(ent.get()))
        else:
            output = divi(1,float(n2.get()))
            n2.set(output)
    else:
        if n1.get() == '':
            if ent.get() == '' or 'ERROR':
                output = 'ERROR' 
            else:
                output = divi(1,float(ent.get()))
        else:
            output = divi(1,float(n1.get()))
            n1.set(output)
    ent.set(str(output))
    
  
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' methods for number buttons and dot '''

def zero():
    if ent.get() == 'ERROR':
        ent.set('')
    global equaled
    if not equaled:
        ent.set('')
        equaled = True
    if turn % 2 == 0:
        n2.set(n2.get() + '0')
        ent.set(ent.get() + '0')
    else:
        n1.set(n1.get() + '0')
        ent.set(ent.get() + '0')
def one():
    if ent.get() == 'ERROR':
        ent.set('')
    global equaled
    if not equaled:
        ent.set('')
        equaled = True
    if turn % 2 == 0:
        n2.set(n2.get() + '1')
        ent.set(ent.get() + '1')
    else:
        n1.set(n1.get() + '1')
        ent.set(ent.get() + '1')
def two():
    if ent.get() == 'ERROR':
        ent.set('')
    global equaled
    if not equaled:
        ent.set('')
        equaled = True
    if turn % 2 == 0:
        n2.set(n2.get() + '2')
        ent.set(ent.get() + '2')
    else:
        n1.set(n1.get() + '2')
        ent.set(ent.get() + '2')
def three():
    if ent.get() == 'ERROR':
        ent.set('')
    global equaled
    if not equaled:
        ent.set('')
        equaled = True
    if turn % 2 == 0:
        n2.set(n2.get() + '3')
        ent.set(ent.get() + '3')
    else:
        n1.set(n1.get() + '3')
        ent.set(ent.get() + '3')
def four():
    if ent.get() == 'ERROR':
        ent.set('')
    global equaled
    if not equaled:
        ent.set('')
        equaled = True
    if turn % 2 == 0:
        n2.set(n2.get() + '4')
        ent.set(ent.get() + '4')
    else:
        n1.set(n1.get() + '4')
        ent.set(ent.get() + '4')
def five():
    if ent.get() == 'ERROR':
        ent.set('')
    global equaled
    if not equaled:
        ent.set('')
        equaled = True
    if turn % 2 == 0:
        n2.set(n2.get() + '5')
        ent.set(ent.get() + '5')
    else:
        n1.set(n1.get() + '5')
        ent.set(ent.get() + '5')
def six():
    if ent.get() == 'ERROR':
        ent.set('')
    global equaled
    if not equaled:
        ent.set('')
        equaled = True
    if turn % 2 == 0:
        n2.set(n2.get() + '6')
        ent.set(ent.get() + '6')
    else:
        n1.set(n1.get() + '6')
        ent.set(ent.get() + '6')
def seven():
    if ent.get() == 'ERROR':
        ent.set('')
    global equaled
    if not equaled:
        ent.set('')
        equaled = True
    if turn % 2 == 0:
        n2.set(n2.get() + '7')
        ent.set(ent.get() + '7')
    else:
        n1.set(n1.get() + '7')
        ent.set(ent.get() + '7')
def eight():
    if ent.get() == 'ERROR':
        ent.set('')
    global equaled
    if not equaled:
        ent.set('')
        equaled = True
    if turn % 2 == 0:
        n2.set(n2.get() + '8')
        ent.set(ent.get() + '8')
    else:
        n1.set(n1.get() + '8')
        ent.set(ent.get() + '8')
def nine():
    if ent.get() == 'ERROR':
        ent.set('')
    global equaled
    if not equaled:
        ent.set('')
        equaled = True
    if turn % 2 == 0:
        n2.set(n2.get() + '9')
        ent.set(ent.get() + '9')
    else:
        n1.set(n1.get() + '9')
        ent.set(ent.get() + '9')
def dot():
    if ent.get() == 'ERROR':
        ent.set('')
    global equaled
    if not equaled:
        ent.set('')
        equaled = True
    if turn % 2 == 0:
        n2.set(n2.get() + '.')
        ent.set(ent.get() + '.')
    else:
        n1.set(n1.get() + '.')
        ent.set(ent.get() + '.')

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' number buttons and entry '''
ent = StringVar()
entry = Entry(root,textvariable=ent,width=30,justify=RIGHT)
entry.grid(column=1,columnspan=4, row=0)

num0 = Button(root,command=zero,text='0',width=5)
num0.grid(column=2,row=6)

num1 = Button(root,command=one,text='1',width=5)
num1.grid(column=1,row=5)

num2 = Button(root,command=two,text='2',width=5)
num2.grid(column=2,row=5)

num3 = Button(root,command=three,text='3',width=5)
num3.grid(column=3,row=5)

num4 = Button(root,command=four,text='4',width=5)
num4.grid(column=1,row=4)

num5 = Button(root,command=five,text='5',width=5)
num5.grid(column=2, row=4)

num6 = Button(root,command=six,text='6',width=5)
num6.grid(column=3,row=4)

num7 = Button(root,command=seven,text='7',width=5)
num7.grid(column=1,row=3)

num8 = Button(root,command=eight,text='8',width=5)
num8.grid(column=2,row=3)

num9 = Button(root,command=nine,text='9',width=5)
num9.grid(column=3, row=3)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''' action buttons '''

plus_btn = Button(root, command=plus, text='+',width=5)
plus_btn.grid(column=4, row=5)

minus_btn = Button(root, command=minus, text='–',width=5)
minus_btn.grid(column=4, row=4)

multi_btn = Button(root, command=times, text='×',width=5)
multi_btn.grid(column=4, row=3)

divi_btn = Button(root, command=divide, text='÷',width=5)
divi_btn.grid(column=4, row=2)

dot_btn = Button(root, command=dot, text='.', width=5)
dot_btn.grid(column=3, row=6)

pwr_btn = Button(root, command=power_set, text='**', width=5)
pwr_btn.grid(column=3, row=2)

sqr_root_btn = Button(root, command=square_root, text='√', width=5)
sqr_root_btn.grid(column=2, row=2)

thr_root_btn = Button(root, command=root3, text='3√', width=5)
thr_root_btn.grid(column=1, row=2)

clear_btn = Button(root, command=clear, text='C', width=5)
clear_btn.grid(column=3, row=1)

clr_all_btn = Button(root, command=clear_all, text='CE', width=5)
clr_all_btn.grid(column=2, row=1)

bksp_btn = Button(root, command=back, text='<<', width=5)
bksp_btn.grid(column=4, row=1)

rec_btn = Button(root, command=rec, text='¹/x', width=5)
rec_btn.grid(column=1, row=1)

eql_btn = Button(root, command=equal,text='=',width=5)
eql_btn.grid(column=4, row=6)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
root.mainloop()

#                                                           BUG LIST
#
#                                                  pressing operators a bit can mess up the turn system                                                                            

