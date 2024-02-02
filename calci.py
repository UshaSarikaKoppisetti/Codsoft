from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, cursor):
        cursor.title("CALCULATOR")
        cursor.geometry('357x420+0+0')
        cursor.config(bg='black')
        cursor.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17, bg='cyan', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        Button(width=12, height=5, text='(', relief='solid', bg='white', command=lambda: self.show('(')).place(x=0, y=50)
        Button(width=12, height=5, text=')', relief='solid', bg='white', command=lambda: self.show(')')).place(x=90, y=50)
        Button(width=12, height=5, text='%', relief='solid', bg='white', command=lambda: self.show('%')).place(x=180, y=50)
        Button(width=12, height=5, text='1', relief='solid', bg='white', command=lambda: self.show(1)).place(x=0, y=125)
        Button(width=12, height=5, text='2', relief='solid', bg='white', command=lambda: self.show(2)).place(x=90, y=125)
        Button(width=12, height=5, text='3', relief='solid', bg='white', command=lambda: self.show(3)).place(x=180, y=125)
        Button(width=12, height=5, text='4', relief='solid', bg='white', command=lambda: self.show(4)).place(x=0, y=200)
        Button(width=12, height=5, text='5', relief='solid', bg='white', command=lambda: self.show(5)).place(x=90, y=200)
        Button(width=12, height=5, text='6', relief='solid', bg='white', command=lambda: self.show(6)).place(x=180, y=200)
        Button(width=12, height=5, text='7', relief='solid', bg='white', command=lambda: self.show(7)).place(x=0, y=275)
        Button(width=12, height=5, text='8', relief='solid', bg='white', command=lambda: self.show(8)).place(x=90, y=275)
        Button(width=12, height=5, text='9', relief='solid', bg='white', command=lambda: self.show(9)).place(x=180, y=275)
        Button(width=12, height=5, text='0', relief='solid', bg='white', command=lambda: self.show(0)).place(x=90, y=350)
        Button(width=12, height=5, text='.', relief='solid', bg='white', command=lambda: self.show('.')).place(x=180, y=350)
        Button(width=12, height=5, text='+', relief='solid', bg='white', command=lambda: self.show('+')).place(x=270, y=275)
        Button(width=12, height=5, text='-', relief='solid', bg='white', command=lambda: self.show('-')).place(x=270, y=200)
        Button(width=12, height=5, text='/', relief='solid', bg='white', command=lambda: self.show('/')).place(x=270, y=50)
        Button(width=12, height=5, text='X', relief='solid', bg='white', command=lambda: self.show('*')).place(x=270, y=125)
        Button(width=12, height=5, text='C', relief='solid', bg='white', command=self.clear).place(x=0, y=350)
        Button(width=12, height=5, text='=', relief='solid', bg='grey', command=self.solve).place(x=270, y=350)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except:
            result = 'Error'
            self.equation.set(result)

root = Tk()
calculator = Calculator(root)
root.mainloop()
