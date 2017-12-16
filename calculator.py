import tkinter
from tkinter import *

gui = tkinter.Tk()
gui.geometry('293x405')
gui.title('Calculator')

class Calculator:

    def varibles(self):
        global start, numberOne, numberTwo, whatDo, result, firstOrSecNumber, howNumber, currentValue, clickNumber, operation, firstOperation
        start = 0
        numberOne = 0
        numberTwo = 0
        whatDo = ''
        result = 0
        firstOrSecNumber = 0
        howNumber = 0
        currentValue = ''
        clickNumber = 10
        operation = 0
        firstOperation = 0

    def calculator(self):
        global start, numberOne, numberTwo, whatDo, result, operation
        if start == 0:
            if whatDo == '+':
                result = float(numberOne) + float(numberTwo)
                print(result)
                guiLabelResult.config(text = result)
                start = 1
            elif whatDo == '-':
                result = float(numberOne) - float(numberTwo)
                print(result)
                guiLabelResult.config(text=result)
                start = 1
            elif whatDo == '*':
                result = float(numberOne) * float(numberTwo)
                print(result)
                guiLabelResult.config(text=result)
                start = 1
            elif whatDo == '/':
                result = float(numberOne) / float(numberTwo)
                print(result)
                guiLabelResult.config(text=result)
                start = 1
        elif start == 1:
            if whatDo == '+':
                result = result + float(numberTwo)
                print(result)
                guiLabelResult.config(text=result)
            elif whatDo == '-':
                result = result - float(numberTwo)
                print(result)
                guiLabelResult.config(text=result)
            elif whatDo == '*':
                result = result * float(numberTwo)
                print(result)
                guiLabelResult.config(text=result)
            elif whatDo == '/':
                result = result / float(numberTwo)
                print(result)
                guiLabelResult.config(text=result)
        operation = 1

    def numberChoose(self):
        global numberOne, numberTwo, howNumber, firstOrSecNumber, currentValue, firstOperation, clickNumber
        if firstOrSecNumber == 0:
            if firstOperation == 0:
                if clickNumber == 1:
                    currentValue += '1'
                    numberOne = float(currentValue)
                    print(numberOne)
                    guiLabelValues.config(text = numberOne)
                elif clickNumber == 2:
                    currentValue += '2'
                    numberOne = float(currentValue)
                    print(numberOne)
                    guiLabelValues.config(text = numberOne)
                elif clickNumber == 3:
                    currentValue += '3'
                    numberOne = float(currentValue)
                    print(numberOne)
                    guiLabelValues.config(text = numberOne)
                elif clickNumber == 4:
                    currentValue += '4'
                    numberOne = float(currentValue)
                    print(numberOne)
                    guiLabelValues.config(text = numberOne)
                elif clickNumber == 5:
                    currentValue += '5'
                    numberOne = float(currentValue)
                    print(numberOne)
                    guiLabelValues.config(text = numberOne)
                elif clickNumber == 6:
                    currentValue += '6'
                    numberOne = float(currentValue)
                    print(numberOne)
                    guiLabelValues.config(text = numberOne)
                elif clickNumber == 7:
                    currentValue += '7'
                    numberOne = float(currentValue)
                    print(numberOne)
                    guiLabelValues.config(text = numberOne)
                elif clickNumber == 8:
                    currentValue += '8'
                    numberOne = float(currentValue)
                    print(numberOne)
                    guiLabelValues.config(text = numberOne)
                elif clickNumber == 9:
                    currentValue += '9'
                    numberOne = float(currentValue)
                    print(numberOne)
                    guiLabelValues.config(text = numberOne)
                elif clickNumber == 0:
                    currentValue += '0'
                    numberOne = float(currentValue)
                    print(numberOne)
                    guiLabelValues.config(text = numberOne)
                elif clickNumber == 20:
                    currentValue += '.'
                    numberOne = float(currentValue)
                    print(numberOne)
                    guiLabelValues.config(text = numberOne)
        elif firstOrSecNumber == 1:
            if clickNumber == 1:
                currentValue += '1'
                numberTwo = float(currentValue)
                howNumber = 1
                print(numberTwo)
                guiLabelValues.config(text = numberTwo)
            elif clickNumber == 2:
                currentValue += '2'
                numberTwo = float(currentValue)
                howNumber = 1
                print(numberTwo)
                guiLabelValues.config(text = numberTwo)
            elif clickNumber == 3:
                currentValue += '3'
                numberTwo = float(currentValue)
                howNumber = 1
                print(numberTwo)
                guiLabelValues.config(text = numberTwo)
            elif clickNumber == 4:
                currentValue += '4'
                numberTwo = float(currentValue)
                howNumber = 1
                print(numberTwo)
                guiLabelValues.config(text = numberTwo)
            elif clickNumber == 5:
                currentValue += '5'
                numberTwo = float(currentValue)
                howNumber = 1
                print(numberTwo)
                guiLabelValues.config(text = numberTwo)
            elif clickNumber == 6:
                currentValue += '6'
                numberTwo = float(currentValue)
                howNumber = 1
                print(numberTwo)
                guiLabelValues.config(text = numberTwo)
            elif clickNumber == 7:
                currentValue += '7'
                numberTwo = float(currentValue)
                howNumber = 1
                print(numberTwo)
                guiLabelValues.config(text = numberTwo)
            elif clickNumber == 8:
                currentValue += '8'
                numberTwo = float(currentValue)
                howNumber = 1
                print(numberTwo)
                guiLabelValues.config(text = numberTwo)
            elif clickNumber == 9:
                currentValue += '9'
                numberTwo = float(currentValue)
                howNumber = 1
                print(numberTwo)
                guiLabelValues.config(text = numberTwo)
            elif clickNumber == 0:
                currentValue += '0'
                numberTwo = float(currentValue)
                howNumber = 1
                print(numberTwo)
                guiLabelValues.config(text = numberTwo)
            elif clickNumber == 20:
                currentValue += '.'
                numberTwo = float(currentValue)
                howNumber = 1
                print(numberTwo)
                guiLabelValues.config(text = numberTwo)

    def number1(self):
        global clickNumber, operation
        clickNumber = 1
        calc.numberChoose()
        operation = 0

    def number2(self):
        global clickNumber, operation
        clickNumber = 2
        calc.numberChoose()
        operation = 0

    def number3(self):
        global clickNumber, operation
        clickNumber = 3
        calc.numberChoose()
        operation = 0

    def number4(self):
        global clickNumber, operation
        clickNumber = 4
        calc.numberChoose()
        operation = 0

    def number5(self):
        global clickNumber, operation
        clickNumber = 5
        calc.numberChoose()
        operation = 0

    def number6(self):
        global clickNumber, operation
        clickNumber = 6
        calc.numberChoose()
        operation = 0

    def number7(self):
        global clickNumber, operation
        clickNumber = 7
        calc.numberChoose()
        operation = 0

    def number8(self):
        global clickNumber, operation
        clickNumber = 8
        calc.numberChoose()
        operation = 0

    def number9(self):
        global clickNumber, operation
        clickNumber = 9
        calc.numberChoose()
        operation = 0

    def number0(self):
        global clickNumber, operation
        clickNumber = 0
        calc.numberChoose()
        operation = 0

    def dot(self):
        global clickNumber, operation
        clickNumber = 20
        calc.numberChoose()
        operation = 0

    def plus(self):
        global whatDo, howNumber, firstOperation, firstOrSecNumber, currentValue, operation
        firstOperation = 1
        firstOrSecNumber = 1
        currentValue = ''
        if operation == 0:
            if howNumber == 1:
                calc.calculator()
            whatDo = '+'

    def minus(self):
        global whatDo, howNumber, firstOperation, firstOrSecNumber, currentValue, operation
        firstOperation = 1
        firstOrSecNumber = 1
        currentValue = ''
        if operation == 0:
            if howNumber == 1:
                calc.calculator()
            whatDo = '-'

    def multiply(self):
        global whatDo, howNumber, firstOperation, firstOrSecNumber, currentValue, operation
        firstOperation = 1
        firstOrSecNumber = 1
        currentValue = ''
        if operation == 0:
            if howNumber == 1:
                calc.calculator()
            whatDo = '*'

    def division(self):
        global whatDo, howNumber, firstOperation, firstOrSecNumber, currentValue, operation
        firstOperation = 1
        firstOrSecNumber = 1
        currentValue = ''
        if operation == 0:
            if howNumber == 1:
                calc.calculator()
            whatDo = '/'

    def squere(self):
        global numberOne, numberTwo, result, start
        if result == 0:
            result = numberOne * numberOne
            print(result)
            guiLabelResult.config(text=result)
            start = 1
        elif result != 0:
            result = result * result
            numberTwo = result
            print(result)
            guiLabelResult.config(text=result)

    def equal(self):
        global whatDo, howNumber, firstOperation, firstOrSecNumber, currentValue, operation
        firstOperation = 1
        if operation == 0:
            if howNumber == 1:
                calc.calculator()
        operation = 0
        clickNumber = 10
        currentValue = ''
        firstOperation = 0
        firstOrSecNumber = 0
        start = 0
        numberOne = 0
        numberTwo = 0
        whatDo = ''
        howNumber = 0

    def resetAll(self):
        global whatDo, howNumber, firstOperation, firstOrSecNumber, currentValue, operation, result, clickNumber, start, numberOne, numberTwo
        firstOperation = 1
        operation = 0
        clickNumber = 10
        currentValue = ''
        firstOperation = 0
        firstOrSecNumber = 0
        start = 0
        numberOne = 0
        numberTwo = 0
        whatDo = ''
        howNumber = 0
        result = 0
        guiLabelResult.config(text=numberOne)
        guiLabelValues.config(text=result)

calc = Calculator()
calc.varibles()
calc.numberChoose()

guiLabelValues = tkinter.Label(gui, text = '0')
guiLabelValues.place(x=20, y=20)

guiLabelResult = tkinter.Label(gui, text = '0')
guiLabelResult.place(x=20, y=35)

guiButtonNegate = tkinter.Button(gui, text = "NEG", height = 3, width = 7)
guiButtonNegate.place(x=20, y=331)

guiButton0 = tkinter.Button(gui, text = "0", command = calc.number0, height = 3, width = 7)
guiButton0.place(x=85, y=331)

guiButtonComma = tkinter.Button(gui, text = ",", command = calc.dot, height = 3, width = 7)
guiButtonComma.place(x=150, y=331)

guiButtonEqual = tkinter.Button(gui, text = "=", command = calc.equal, height = 3, width = 7)
guiButtonEqual.place(x=215, y=331)

guiButton1 = tkinter.Button(gui, text = "1", command = calc.number1, height = 3, width = 7)
guiButton1.place(x=20, y=270)

guiButton2 = tkinter.Button(gui, text = "2", command = calc.number2, height = 3, width = 7)
guiButton2.place(x=85, y=270)

guiButton3 = tkinter.Button(gui, text = "3", command = calc.number3, height = 3, width = 7)
guiButton3.place(x=150, y=270)

guiButtonPlus = tkinter.Button(gui, text = "+", command = calc.plus, height = 3, width = 7)
guiButtonPlus.place(x=215, y=270)

guiButton4 = tkinter.Button(gui, text = "4", command = calc.number4, height = 3, width = 7)
guiButton4.place(x=20, y=209)

guiButton5 = tkinter.Button(gui, text = "5", command = calc.number5, height = 3, width = 7)
guiButton5.place(x=85, y=209)

guiButton6 = tkinter.Button(gui, text = "6", command = calc.number6, height = 3, width = 7)
guiButton6.place(x=150, y=209)

guiButtonMinus = tkinter.Button(gui, text = "-", command = calc.minus, height = 3, width = 7)
guiButtonMinus.place(x=215, y=209)

guiButton7 = tkinter.Button(gui, text = "7", command = calc.number7, height = 3, width = 7)
guiButton7.place(x=20, y=148)

guiButton8 = tkinter.Button(gui, text = "8", command = calc.number8, height = 3, width = 7)
guiButton8.place(x=85, y=148)

guiButton9 = tkinter.Button(gui, text = "9", command = calc.number9, height = 3, width = 7)
guiButton9.place(x=150, y=148)

guiButtonMultiply = tkinter.Button(gui, text = "x", height = 3, width = 7)
guiButtonMultiply.place(x=215, y=148)

guiButtonPercent = tkinter.Button(gui, text = "%", height = 3, width = 7)
guiButtonPercent.place(x=20, y=87)

guiButtonSquere = tkinter.Button(gui, text = "Squere", command = calc.squere, height = 3, width = 7)
guiButtonSquere.place(x=85, y=87)

guiButtonC = tkinter.Button(gui, text = "C", command = calc.resetAll, height = 3, width = 7)
guiButtonC.place(x=150, y=87)

guiButtonDivision = tkinter.Button(gui, text = "/", command = calc.division, height = 3, width = 7)
guiButtonDivision.place(x=215, y=87)

guiButtonMultiply = tkinter.Button(gui, text = "x", command = calc.multiply, height = 3, width = 7)
guiButtonMultiply.place(x=215, y=148)

gui.mainloop()
