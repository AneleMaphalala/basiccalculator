from math import sqrt
from tkinter import *

expression = "" 

def press(num): 
	global expression 
	expression = expression + str(num) 
	equation.set(expression) 


def equalpress(): 
	try: 

		global expression 
		total = str(eval(expression)) 
		equation.set(total) 
		expression = "" 
	except: 

		equation.set("INVALID") 
		expression = "" 
 
def clear(): 
	global expression 
	expression = "" 
	equation.set("") 

def sqrt_press():
    try:
        global expression
        result = sqrt(eval(expression))
        equation.set(result)
        expression = str(result)
    except:
        equation.set("INVALID")
        expression = ""

if __name__ == "__main__": 
	win = Tk() 

	win.configure(background="black") 
	win.title("Simple Calculator") 
	win.geometry("400x300") 
	
	equation = StringVar() 
 
	expression_field = Entry(win, textvariable=equation)  
	expression_field.grid(columnspan=50, ipadx=124) 
    
	clear = Button(win, text='C', fg='black', bg='light grey', 
				command=clear, height=2, width=12) 
	clear.grid(row=2, column='0') 

button_negative= Button(win,text='+/-',fg='black',bg='light grey',
							command=lambda:press('-'),height=2,width=12)
button_negative.grid(row=2,column='1')

button_percentage = Button(win,text='%',fg='black',bg='light grey',
                        command=lambda:press('%'),height=2,width=12)
button_percentage.grid(row=2,column='2')

button_7 = Button(win, text='7', fg='black', bg='grey', 
                    command=lambda: press(7), height=2, width=12) 
button_7.grid(row=3, column=0) 

button_8 = Button(win, text='8', fg='black', bg='grey', 
                    command=lambda: press(8), height=2, width=12) 
button_8.grid(row=3, column=1) 

button_9 = Button(win, text='9', fg='black', bg='grey', 
                    command=lambda: press(9), height=2, width=12) 
button_9.grid(row=3, column=2) 

multiply = Button(win, text=' * ', fg='black', bg='orange', 
					command=lambda: press("*"), height=2, width=12) 
multiply.grid(row=3, column=3) 

divide = Button(win, text=' / ', fg='black', bg='orange', 
					command=lambda: press("/"), height=2, width=12) 
divide.grid(row=2, column=3) 

button_4 = Button(win, text='4', fg='black', bg='grey', 
                    command=lambda: press(4), height=2, width=12) 
button_4.grid(row=4, column=0) 

button_5 = Button(win, text='5', fg='black', bg='grey', 
                    command=lambda: press(5), height=2, width=12) 
button_5.grid(row=4, column=1) 

button_6 = Button(win, text='6', fg='black', bg='grey', 
                    command=lambda: press(6), height=2, width=12) 
button_6.grid(row=4, column=2) 

button_subtraction = Button(win, text=' - ', fg='black', bg='orange', 
				command=lambda: press("-"), height=2, width=12) 
button_subtraction.grid(row=4,column=3)

button_1 = Button(win, text='1', fg='black', bg='grey', 
                    command=lambda: press(1), height=2, width=12) 
button_1.grid(row=5, column=0) 

button_2 = Button(win, text='2', fg='black', bg='grey', 
                    command=lambda: press(2), height=2, width=12) 
button_2.grid(row=5, column=1) 

button_3 = Button(win, text='3', fg='black', bg='grey', 
                    command=lambda: press(3), height=2, width=12) 
button_3.grid(row=5, column=2) 

button_addition = Button(win, text=' + ', fg='black', bg='orange', 
            command=lambda: press("+"), height=2, width=12) 
button_addition.grid(row=5, column=3) 

button_0 = Button(win, text='0', fg='black', bg='grey', 
                    command=lambda: press(0), height=2, width=12) 
button_0.grid(row=6, column=0) 


Decimal= Button(win, text=',', fg='black', bg='grey', 
					command=lambda: press('.'), height=2, width=12) 
Decimal.grid(row=6, column=1) 

sqrt_button = Button(win, text='√', fg='black', bg='light grey',
                    command=sqrt_press, height=2, width=12)
sqrt_button.grid(row=6, column=2)

equal = Button(win, text=' = ', fg='black', bg='orange', 
				command=equalpress, height=2, width=12) 
equal.grid(row=6, column=3,columnspan=2)

blank = Button(win, text='  ', fg='black', bg='orange', 
				 height=2, width=12) 
equal.grid(row=6, column=3,columnspan=2)


win.mainloop() 