import tkinter as tk
import math
root = tk.Tk()
root.title("Calculator")
root.geometry("720x410")
d=""
operator_index=0
e=""
text1=""
menu1=tk.Menu()
root.config(menu=menu1)
def Ans():
    global text1
    text1 = display_output["text"]
    display_input.config(text=text1)
    display_output.config(text="")
    global d,firstNum,operator,secondNum
    firstNum,operator,secondNum=0,0,0
    firstNum=str(firstNum)
    operator=str(operator)
    secondNum=str(secondNum)
    firstNum,operator,secondNum,d="","","",""
    d=text1
    enable()
def disable():
    plus_button.config(state=tk.DISABLED)
    minus_button.config(state=tk.DISABLED)
    multiply_button.config(state=tk.DISABLED)
    divide_button.config(state=tk.DISABLED)
    power_button.config(state=tk.DISABLED)
def enable():
    plus_button.config(state=tk.NORMAL)
    minus_button.config(state=tk.NORMAL)
    multiply_button.config(state=tk.NORMAL)
    divide_button.config(state=tk.NORMAL)
    power_button.config(state=tk.NORMAL)

def click(b):
    global d
    d+=b["text"]
    enable()
    if b["text"]==" + " or b["text"]==" - " or b["text"]==" x " or b["text"]==" / " or b["text"]=="^":
      disable()
    d=d.replace(" ","")
    display_input["text"]+= b["text"]

def dell():
    global d
    d=d[0:(len(d)-1)]
    display_input.config(text=d)

def output():
    global operator_index,firstNum,operator,secondNum
    operator_index = None
    for i, char in enumerate(d):
        if char in ["+", "-", "x", "/", "^"]:
          
            operator_index=i
            break
        else:
            display_output.config(text="Cannot handle command with more than one operator")
    if operator_index is None:
        display_output.config(text="Invalid input")
        return
    firstNum = d[:operator_index]
    operator = d[operator_index]
    secondNum = d[operator_index + 1:]
    firstNum=float(firstNum)
    secondNum = float(secondNum)
    if operator=="+":
        answer=firstNum + secondNum
    elif operator=="-":
        answer=firstNum-secondNum
    elif operator=="x":
        answer=firstNum*secondNum
    elif operator=="/" and secondNum!=0:
        answer=firstNum/secondNum
    elif operator=="^":
        answer = (firstNum)**(secondNum)
    elif operator=="/" and secondNum==0:
        display_output.config(text="Math Error <3")
    answer=str(answer)
    display_output.config(text=answer)
    disable()

def reset():
    global d,firstNum,operator,secondNum
    firstNum,operator,secondNum=0,0,0
    firstNum=str(firstNum)
    operator=str(operator)
    secondNum=str(secondNum)
    firstNum,operator,secondNum,d="","","",""
    display_input.config(text="")
    display_output.config(text="")
    disable()

display_input = tk.Label(root, text="", height=2, width=45, bg="pink",borderwidth=4 , font=("helvetica", 20))
display_input.grid(row=0, column=0, columnspan=5)

display_output = tk.Label(root, text="", height=2, width=45, bg="pink",borderwidth=4 , font=("helvetica", 20))
display_output.grid(row=1, column=0, columnspan=5)

global b5
b1 = tk.Button(root, font=("Helvetica",15),text="7", height=2, width=12,borderwidth=4 ,command = lambda: click(b1))
b2 = tk.Button(root,font=("Helvetica",15), text="8", height=2, width=12,borderwidth=4 ,command = lambda: click(b2))
b3 = tk.Button(root,font=("Helvetica",15), text="9", height=2, width=12,borderwidth=4 ,command = lambda: click(b3))
plus_button = tk.Button(root,font=("Helvetica",15), text=" + ", height=2, width=12,borderwidth=4 , command = lambda: click(plus_button))
minus_button = tk.Button(root,font=("Helvetica",15), text=" - ", height=2, width=12,borderwidth=4 , command = lambda: click(minus_button))

b6 = tk.Button(root,font=("Helvetica",15), text="4", height=2, width=12,borderwidth=4 , command = lambda: click(b6))
b7 = tk.Button(root,font=("Helvetica",15), text="5", height=2, width=12,borderwidth=4 , command = lambda: click(b7))
b8 = tk.Button(root,font=("Helvetica",15), text="6", height=2, width=12,borderwidth=4 , command = lambda: click(b8))
multiply_button = tk.Button(root,font=("Helvetica",15), text=" x ", height=2, width=12, borderwidth=4 ,command = lambda: click(multiply_button))
divide_button = tk.Button(root,font=("Helvetica",15), text=" / ", height=2, width=12,borderwidth=4 , command = lambda: click(divide_button))

b11 = tk.Button(root,font=("Helvetica",15), text="1", height=2, width=12,borderwidth=4 , command = lambda: click(b11))
b12 = tk.Button(root,font=("Helvetica",15), text="2", height=2, width=12,borderwidth=4 , command = lambda: click(b12))
b13 = tk.Button(root,font=("Helvetica",15), text="3", height=2, width=12,borderwidth=4 , command = lambda: click(b13))
equal_button = tk.Button(root,font=("Helvetica",15), text="=", height=2, width=12,borderwidth=4 , command = output)
delete_button = tk.Button(root,font=("Helvetica",15), text="del", height=2, width=12,borderwidth=4 , command = dell)

b16 = tk.Button(root, font=("Helvetica",15),text="0", height=2, width=12,borderwidth=4 ,command = lambda: click(b16))
b17 = tk.Button(root,font=("Helvetica",15), text=":)", height=2, width=12,borderwidth=4 ,command = lambda: click())
b18 = tk.Button(root,font=("Helvetica",15), text="Ans", height=2, width=12,borderwidth=4 ,command = Ans)
power_button = tk.Button(root,font=("Helvetica",15), text="^", height=2, width=12,borderwidth=4 , command = lambda: click(power_button))
decimal_button = tk.Button(root,font=("Helvetica",15), text=".", height=2, width=12,borderwidth=4 , command = lambda: click(decimal_button))

b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3.grid(row=2, column=2)
plus_button.grid(row=2, column=3)
minus_button.grid(row=2, column=4)

b6.grid(row=3, column=0)
b7.grid(row=3, column=1)
b8.grid(row=3, column=2)
multiply_button.grid(row=3, column=3)
divide_button.grid(row=3, column=4)

b11.grid(row=4, column=0)
b12.grid(row=4, column=1)
b13.grid(row=4, column=2)
equal_button.grid(row=4, column=3)
delete_button.grid(row=4, column=4)

b16.grid(row=5, column=0)
b17.grid(row=5, column=1)
b18.grid(row=5, column=2)
power_button.grid(row=5, column=3)
decimal_button.grid(row=5, column=4)

file_menu=tk.Menu(menu1)
menu1.add_cascade(label="New", menu=file_menu)
file_menu.add_command(label="Reset", command=reset)

disable()
root.mainloop()
