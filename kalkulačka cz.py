from tkinter import *
import math
import parser
import random

window = Tk()
window.title("Kalkulačka")
window.geometry("320x430+0+0")
window.configure(bg = "#157879")
window.resizable(width= False , height= False)

expression = ""
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def klasicka():
    window.resizable(width = False, height = False)
    window.geometry("320x430+0+0")
    expression_field.grid(row=0, column=0, columnspan=4, ipadx=8,ipady=8,pady=8)

def rozsirena():
    window.resizable(width = False, height = False)
    window.geometry("700x430+0+0")
    expression_field.grid(row=0, column=0, columnspan=180, ipadx=180,ipady=8,pady=8)

def clear():
    global expression
    expression = ""
    equation.set("0")

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Neočekávaný problém",)
        expression = "" 

def sin():
    global expression
    expression = float(expression)
    expression = round(math.sin(math.radians(expression)), 5)
    equation.set(float(expression))
    expression = str(expression)

def cos():
    global expression
    expression = float(expression)
    expression = round(math.cos(math.radians(expression)), 5)
    equation.set(float(expression))
    expression = str(expression)

def tan():
    global expression
    expression = float(expression)
    expression = round(math.tan(math.radians(expression)), 5)
    equation.set(float(expression))
    expression = str(expression)

def acos():
    global expression
    expression = float(expression)
    expression = round((math.acos(expression)) * (180 / math.pi), 3)
    equation.set(float(expression))
    expression = str(expression)

def atan():
    global expression
    expression = float(expression)
    expression = round((math.atan(expression)) * (180 / math.pi), 3)
    equation.set(float(expression))
    expression = str(expression)

def asin():
    global expression
    expression = float(expression)
    expression = round((math.asin(expression)) * (180 / math.pi), 3)
    equation.set(float(expression))
    expression = str(expression)

def sqrt():
    global expression
    expression = float(expression)
    expression = math.sqrt(expression)
    equation.set(float(expression))
    expression = str(expression)

def log1():
    global expression
    expression = float(expression)
    expression = math.log(expression)
    equation.set(float(expression))
    expression = str(expression)

def log2():
    global expression
    expression = float(expression)
    expression = math.log2(expression)
    equation.set(float(expression))
    expression = str(expression)

def exp():
    global expression
    expression = float(expression)
    expression = math.exp(expression)
    equation.set(float(expression))
    expression = str(expression)

def gamma():
    global expression
    expression = float(expression)
    expression = math.gamma(expression)
    equation.set(float(expression))
    expression = str(expression)

def erf():
    global expression
    expression = float(expression)
    expression = math.erf(expression)
    equation.set(float(expression))
    expression = str(expression)

def factorial():
    global expression
    expression = float(expression)
    expression = math.factorial(expression)
    equation.set(float(expression))
    expression = str(expression)

def floor():
    global expression
    expression = float(expression)
    expression = math.floor(expression)
    equation.set(float(expression))
    expression = str(expression)

def lgamma():
    global expression
    expression = float(expression)
    expression = math.lgamma(expression)
    equation.set(float(expression))
    expression = str(expression)

calc = Menu(window)
menubar = Menu(calc)
filemenu = Menu(menubar,tearoff =False)
menubar.add_cascade(label = "Kalkulačky", menu=filemenu)
filemenu.add_command(label = "Klasická", command = klasicka)
filemenu.add_command(label = "Rozšířená", command = rozsirena)
filemenu.add_separator()

button_frame = Frame(window,bg="#157879")
button_frame.pack()

equation = StringVar()
equation.set("0")
expression_field = Entry(button_frame,state=DISABLED,textvariable = equation,justify="right",font=("arial",20,"bold",))
    
button1 = Button(button_frame,text="1",font=("arial",12), relief="ridge",bd="1", bg="#27CFD1",width=8, height=3, command=lambda:press(1))
button2 = Button(button_frame,text="2",font=("arial",12), relief="ridge",bd="1", bg="#27CFD1",width=8, height=3, command=lambda:press(2))
button3 = Button(button_frame,text="3",font=("arial",12), relief="ridge",bd="1", bg="#27CFD1",width=8, height=3, command=lambda:press(3))
scitani = Button(button_frame,text="+",font=("arial",12), relief="ridge",bd="1", bg="#27CFD1",width=8, height=3, command=lambda:press("+"))
button5 = Button(button_frame,text="4",font=("arial",12), relief="ridge",bd="1", bg="#27CFD1",width=8, height=3, command=lambda:press(4))
button6 = Button(button_frame,text="5",font=("arial",12), relief="ridge",bd="1", bg="#27CFD1",width=8, height=3, command=lambda:press(5))
button7 = Button(button_frame,text="6",font=("arial",12), relief="ridge",bd="1", bg="#27CFD1",width=8, height=3, command=lambda:press(6))
odcitani = Button(button_frame,text="-",font=("arial",12), relief="ridge",bd="1", bg="#27CFD1",width=8, height=3, command=lambda:press("-"))
button9 = Button(button_frame,text="7",font=("arial",12), relief="ridge",bd="1", bg="#27CFD1",width=8, height=3, command=lambda:press(7))
button10 = Button(button_frame,text="8",font=("arial",12), relief="ridge",bd="1", bg="#27CFD1",width=8, height=3, command=lambda:press(8))
button11 = Button(button_frame,text="9",font=("arial",12), relief="ridge",bd="1", bg="#27CFD1",width=8, height=3, command=lambda:press(9))
nasobeni = Button(button_frame,text="*",font=("arial",12), relief="ridge",bd="1", bg="#27CFD1",width=8, height=3, command=lambda:press("*"))
button13 = Button(button_frame,text="0",font=("arial",12), relief="ridge",bd="1", bg="#27CFD1",width=8, height=3, command=lambda:press(0))
deleni = Button(button_frame,text="/",font=("arial",12), relief="ridge",bd="1", bg="#27CFD1",width=8, height=3, command=lambda:press("/"))
carka = Button(button_frame,text=".",font=("arial",12), relief="ridge",bd="1", bg="#27CFD1",width=8, height=3, command=lambda:press("."))
smazat = Button(button_frame,text="C",font=("arial",12), relief="ridge",bd="1", bg="#27CFD1",width=8, height=3, command=clear)
rovna = Button(button_frame,text="=",font=("arial",12), relief="ridge",bd="1", bg="#3BA5A6",width=32, height=3, command=equalpress)

pi = Button(button_frame,text="Π",font=("arial",12), relief="ridge",bd="1", bg="#38C4C5",width=8, height=3, command=lambda:press("3.14"))
e = Button(button_frame,text="e",font=("arial",12), relief="ridge",bd="1", bg="#38C4C5",width=8, height=3, command=lambda:press("2.72"))
cos = Button(button_frame,text="cos",font=("arial",12), relief="ridge",bd="1", bg="#38C4C5",width=8, height=3, command=cos)
tan = Button(button_frame,text="tan",font=("arial",12), relief="ridge",bd="1", bg="#38C4C5",width=8, height=3, command=tan)
sin = Button(button_frame,text="sin",font=("arial",12), relief="ridge",bd="1", bg="#38C4C5",width=8, height=3, command=sin)
acos = Button(button_frame,text="acos",font=("arial",12), relief="ridge",bd="1", bg="#38C4C5",width=8, height=3, command=acos)
atan = Button(button_frame,text="atan",font=("arial",12), relief="ridge",bd="1", bg="#38C4C5",width=8, height=3, command=atan)
asin = Button(button_frame,text="asin",font=("arial",12), relief="ridge",bd="1", bg="#38C4C5",width=8, height=3, command=asin)
sqrt = Button(button_frame,text="√",font=("arial",12), relief="ridge",bd="1", bg="#38C4C5",width=8, height=3, command=sqrt)
moc = Button(button_frame,text="**",font=("arial",12), relief="ridge",bd="1", bg="#38C4C5",width=8, height=3, command=lambda:press("**"))
button14 = Button(button_frame,text="00",font=("arial",12), relief="ridge",bd="1", bg="#38C4C5",width=8, height=3, command=lambda:press("00"))
button15 = Button(button_frame,text="000",font=("arial",12), relief="ridge",bd="1", bg="#38C4C5",width=8, height=3, command=lambda:press("000"))
log1 = Button(button_frame,text="log",font=("arial",12), relief="ridge",bd="1", bg="#38C4C5",width=8, height=3, command=log1)
log2 = Button(button_frame,text="log2",font=("arial",12), relief="ridge",bd="1", bg="#38C4C5",width=8, height=3, command=log2)
exp = Button(button_frame,text="Exp",font=("arial",12), relief="ridge",bd="1", bg="#38C4C5",width=8, height=3, command=exp)
gamma = Button(button_frame,text="gamma",font=("arial",12), relief="ridge",bd="1", bg="#38C4C5",width=8, height=3, command=gamma)
erf = Button(button_frame,text="erf",font=("arial",12), relief="ridge",bd="1", bg="#38C4C5",width=8, height=3, command=erf)
fac = Button(button_frame,text="factorial",font=("arial",12), relief="ridge",bd="1", bg="#38C4C5",width=8, height=3, command=factorial)
floor = Button(button_frame,text="floor",font=("arial",12), relief="ridge",bd="1", bg="#38C4C5",width=8, height=3, command=floor)
lgamma = Button(button_frame,text="lgamma",font=("arial",12), relief="ridge",bd="1", bg="#38C4C5",width=8, height=3, command=lgamma)

expression_field.grid(row=0, column=0, columnspan=4, ipadx=8,ipady=8,pady=8)

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
scitani.grid(row=1, column=3)

button5.grid(row=2, column=0)
button6.grid(row=2, column=1)
button7.grid(row=2, column=2)
odcitani.grid(row=2, column=3)

button9.grid(row=3, column=0)
button10.grid(row=3, column=1)
button11.grid(row=3, column=2)
nasobeni.grid(row=3, column=3)

deleni.grid(row=4, column=0)
button13.grid(row=4, column=1)
smazat.grid(row=4, column=2)
carka.grid(row=4, column=3)

pi.grid(row=1, column=5)
e.grid(row=4, column=7)
sqrt.grid(row=2, column=5)
moc.grid(row=3, column=5)
cos.grid(row=1, column=6)
tan.grid(row=1, column=7)
sin.grid(row=1, column=8)
acos.grid(row=2, column=6)
atan.grid(row=2, column=7)
asin.grid(row=2, column=8)
button14.grid(row=4, column=5)
button15.grid(row=4, column=6)
log1.grid(row=3, column=6)
log2.grid(row=3, column=7)
exp.grid(row=3, column=8)
gamma.grid(row=4, column=8)
erf.grid(row=5, column=5)
fac.grid(row=5, column=7)
floor.grid(row=5, column=6)
lgamma.grid(row=5, column=8)

rovna.grid(row=5, column=0, columnspan=4)

window.config(menu = menubar)
window.mainloop()