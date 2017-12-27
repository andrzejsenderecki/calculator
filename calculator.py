import tkinter
from tkinter import *

gui = tkinter.Tk()
gui.geometry('295x405')
gui.title('Calculator')

class CreateVaribles:
    def varibles(self):
        global start, numberOne, numberTwo, whatDo, result, firstOrSecNumber, howNumber, currentValue, clickNumber, operation, firstOperation, plus, minus, multiply, division, doubleClickPlus, doubleClickMinus, doubleClickMultiply, doubleClickDivision
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
        plus = 0
        minus = 0
        multiply = 0
        division = 0
        doubleClickPlus = 0
        doubleClickMinus = 0
        doubleClickMultiply = 0
        doubleClickDivision = 0

class Calculator:
    def calculator(self):
        global start, numberOne, numberTwo, whatDo, result, operation, plus, minus, multiply, division, numberClickPlus, numberClickMinus, doubleClickMultiply, doubleClickDivision
        if start == 0:
            if whatDo == '+':
                result = float(numberOne) + float(numberTwo)
                guiLabelResult.config(text = 'Equals:    ' + str(result))
                start = 1
                plus = 0
                minus = 0
                multiply = 0
                division = 0
            elif whatDo == '-':
                result = float(numberOne) - float(numberTwo)
                guiLabelResult.config(text = 'Equals:    ' + str(result))
                start = 1
                plus = 0
                minus = 0
                multiply = 0
                division = 0
            elif whatDo == '*':
                result = float(numberOne) * float(numberTwo)
                guiLabelResult.config(text = 'Equals:    ' + str(result))
                start = 1
                plus = 0
                minus = 0
                multiply = 0
                division = 0
            elif whatDo == '/':
                result = float(numberOne) / float(numberTwo)
                guiLabelResult.config(text = 'Equals:    ' + str(result))
                start = 1
                plus = 0
                minus = 0
                multiply = 0
                division = 0
        elif start == 1:
            if whatDo == '+':
                result = result + float(numberTwo)
                guiLabelResult.config(text = 'Equals:    ' + str(result))
                plus = 0
                minus = 0
                multiply = 0
                division = 0
            elif whatDo == '-':
                result = result - float(numberTwo)
                guiLabelResult.config(text = 'Equals:    ' + str(result))
                plus = 0
                minus = 0
                multiply = 0
                division = 0
            elif whatDo == '*':
                result = result * float(numberTwo)
                guiLabelResult.config(text = 'Equals:    ' + str(result))
                plus = 0
                minus = 0
                multiply = 0
                division = 0
            elif whatDo == '/':
                result = result / float(numberTwo)
                guiLabelResult.config(text = 'Equals:    ' + str(result))
                plus = 0
                minus = 0
                multiply = 0
                division = 0
        operation = 1

class WhichNumber:
    def numberChoose(self):
        global numberOne, numberTwo, howNumber, firstOrSecNumber, currentValue, firstOperation, clickNumber
        if firstOrSecNumber == 0:
            if firstOperation == 0:
                if clickNumber == 1:
                    currentValue += '1'
                    numberOne = float(currentValue)
                    guiLabelValues.config(text = 'Current number:    ' + str(numberOne))
                elif clickNumber == 2:
                    currentValue += '2'
                    numberOne = float(currentValue)
                    guiLabelValues.config(text = 'Current number:    ' + str(numberOne))
                elif clickNumber == 3:
                    currentValue += '3'
                    numberOne = float(currentValue)
                    guiLabelValues.config(text = 'Current number:    ' + str(numberOne))
                elif clickNumber == 4:
                    currentValue += '4'
                    numberOne = float(currentValue)
                    guiLabelValues.config(text = 'Current number:    ' + str(numberOne))
                elif clickNumber == 5:
                    currentValue += '5'
                    numberOne = float(currentValue)
                    guiLabelValues.config(text = 'Current number:    ' + str(numberOne))
                elif clickNumber == 6:
                    currentValue += '6'
                    numberOne = float(currentValue)
                    guiLabelValues.config(text = 'Current number:    ' + str(numberOne))
                elif clickNumber == 7:
                    currentValue += '7'
                    numberOne = float(currentValue)
                    guiLabelValues.config(text = 'Current number:    ' + str(numberOne))
                elif clickNumber == 8:
                    currentValue += '8'
                    numberOne = float(currentValue)
                    guiLabelValues.config(text = 'Current number:    ' + str(numberOne))
                elif clickNumber == 9:
                    currentValue += '9'
                    numberOne = float(currentValue)
                    guiLabelValues.config(text = 'Current number:    ' + str(numberOne))
                elif clickNumber == 0:
                    currentValue += '0'
                    numberOne = float(currentValue)
                    guiLabelValues.config(text = 'Current number:    ' + str(numberOne))
                elif clickNumber == 20:
                    currentValue += '.'
                    numberOne = float(currentValue)
                    guiLabelValues.config(text = 'Current number:    ' + str(numberOne))
        elif firstOrSecNumber == 1:
            if clickNumber == 1:
                currentValue += '1'
                numberTwo = float(currentValue)
                howNumber = 1
                guiLabelValues.config(text = 'Current number:    ' + str(numberTwo))
            elif clickNumber == 2:
                currentValue += '2'
                numberTwo = float(currentValue)
                howNumber = 1
                guiLabelValues.config(text = 'Current number:    ' + str(numberTwo))
            elif clickNumber == 3:
                currentValue += '3'
                numberTwo = float(currentValue)
                howNumber = 1
                guiLabelValues.config(text = 'Current number:    ' + str(numberTwo))
            elif clickNumber == 4:
                currentValue += '4'
                numberTwo = float(currentValue)
                howNumber = 1
                guiLabelValues.config(text = 'Current number:    ' + str(numberTwo))
            elif clickNumber == 5:
                currentValue += '5'
                numberTwo = float(currentValue)
                howNumber = 1
                guiLabelValues.config(text = 'Current number:    ' + str(numberTwo))
            elif clickNumber == 6:
                currentValue += '6'
                numberTwo = float(currentValue)
                howNumber = 1
                guiLabelValues.config(text = 'Current number:    ' + str(numberTwo))
            elif clickNumber == 7:
                currentValue += '7'
                numberTwo = float(currentValue)
                howNumber = 1
                guiLabelValues.config(text = 'Current number:    ' + str(numberTwo))
            elif clickNumber == 8:
                currentValue += '8'
                numberTwo = float(currentValue)
                howNumber = 1
                guiLabelValues.config(text = 'Current number:    ' + str(numberTwo))
            elif clickNumber == 9:
                currentValue += '9'
                numberTwo = float(currentValue)
                howNumber = 1
                guiLabelValues.config(text = 'Current number:    ' + str(numberTwo))
            elif clickNumber == 0:
                currentValue += '0'
                numberTwo = float(currentValue)
                howNumber = 1
                guiLabelValues.config(text = 'Current number:    ' + str(numberTwo))
            elif clickNumber == 20:
                currentValue += '.'
                numberTwo = float(currentValue)
                howNumber = 1
                guiLabelValues.config(text = 'Current number:    ' + str(numberTwo))

class Numbers:
    def number1(self):
        global clickNumber, operation
        clickNumber = 1
        counterNumber.numberChoose()
        operation = 0

    def number2(self):
        global clickNumber, operation
        clickNumber = 2
        counterNumber.numberChoose()
        operation = 0

    def number3(self):
        global clickNumber, operation
        clickNumber = 3
        counterNumber.numberChoose()
        operation = 0

    def number4(self):
        global clickNumber, operation
        clickNumber = 4
        counterNumber.numberChoose()
        operation = 0

    def number5(self):
        global clickNumber, operation
        clickNumber = 5
        counterNumber.numberChoose()
        operation = 0

    def number6(self):
        global clickNumber, operation
        clickNumber = 6
        counterNumber.numberChoose()
        operation = 0

    def number7(self):
        global clickNumber, operation
        clickNumber = 7
        counterNumber.numberChoose()
        operation = 0

    def number8(self):
        global clickNumber, operation
        clickNumber = 8
        counterNumber.numberChoose()
        operation = 0

    def number9(self):
        global clickNumber, operation
        clickNumber = 9
        counterNumber.numberChoose()
        operation = 0

    def number0(self):
        global clickNumber, operation
        clickNumber = 0
        counterNumber.numberChoose()
        operation = 0

    def dot(self):
        global clickNumber, operation
        clickNumber = 20
        counterNumber.numberChoose()
        operation = 0

class Operations:
    def plus(self):
        global whatDo, howNumber, firstOperation, firstOrSecNumber, currentValue, operation, plus, minus, multiply, division, doubleClickPlus, doubleClickMinus, doubleClickMultiply, doubleClickDivision
        doubleClickPlus += 1
        plus = 1
        firstOperation = 1
        firstOrSecNumber = 1
        currentValue = ''
        if minus == 1:
            whatDo = '-'
        elif multiply == 1:
            whatDo = '*'
        elif division == 1:
            whatDo = '/'
        if doubleClickPlus == 2:
            whatDo = '+'
            doubleClickPlus = 0
            doubleClickMinus = 0
            doubleClickMultiply = 0
            doubleClickDivision = 0
        if doubleClickMinus == 1:
            doubleClickMinus = 0
        if doubleClickMultiply == 1:
            doubleClickMultiply = 0
        if doubleClickDivision == 1:
            doubleClickDivision = 0
        if operation == 0:
            if howNumber == 1:
                calc.calculator()
            whatDo = '+'

    def minus(self):
        global whatDo, howNumber, firstOperation, firstOrSecNumber, currentValue, operation, numberOne, plus, minus, multiply, division, doubleClickPlus, doubleClickMinus, doubleClickMultiply, doubleClickDivision
        doubleClickMinus += 1
        minus = 1
        firstOperation = 1
        firstOrSecNumber = 1
        currentValue = ''
        if plus == 1:
            whatDo = '+'
        elif multiply == 1:
            whatDo = '*'
        elif division == 1:
            whatDo = '/'
        if doubleClickMinus == 2:
            whatDo = '-'
            doubleClickPlus = 0
            doubleClickMinus = 0
            doubleClickMultiply = 0
            doubleClickDivision = 0
        if doubleClickPlus == 1:
            doubleClickPlus = 0
        if doubleClickMultiply == 1:
            doubleClickMultiply = 0
        if doubleClickDivision == 1:
            doubleClickDivision = 0
        if operation == 0:
            if howNumber == 1:
                calc.calculator()
            whatDo = '-'

    def multiply(self):
        global whatDo, howNumber, firstOperation, firstOrSecNumber, currentValue, operation, plus, minus, multiply, division, doubleClickPlus, doubleClickMinus, doubleClickMultiply, doubleClickDivision
        doubleClickMultiply += 1
        multiply = 1
        firstOperation = 1
        firstOrSecNumber = 1
        currentValue = ''
        if plus == 1:
            whatDo = '+'
        elif minus == 1:
            whatDo = '-'
        elif division == 1:
            whatDo = '/'
        if doubleClickMultiply == 2:
            whatDo = '*'
            doubleClickPlus = 0
            doubleClickMinus = 0
            doubleClickMultiply = 0
            doubleClickDivision = 0
        if doubleClickPlus == 1:
            doubleClickPlus = 0
        if doubleClickMinus == 1:
            doubleClickMinus = 0
        if doubleClickDivision == 1:
            doubleClickDivision = 0
        if operation == 0:
            if howNumber == 1:
                calc.calculator()
            whatDo = '*'

    def division(self):
        global whatDo, howNumber, firstOperation, firstOrSecNumber, currentValue, operation, plus, minus, multiply, division, doubleClickPlus, doubleClickMinus, doubleClickMultiply, doubleClickDivision
        doubleClickDivision += 1
        division = 1
        firstOperation = 1
        firstOrSecNumber = 1
        currentValue = ''
        if plus == 1:
            whatDo = '+'
        elif minus == 1:
            whatDo = '-'
        elif multiply == 1:
            whatDo = '*'
        if doubleClickDivision == 2:
            whatDo = '/'
            doubleClickPlus = 0
            doubleClickMinus = 0
            doubleClickMultiply = 0
            doubleClickDivision = 0
        if doubleClickPlus == 1:
            doubleClickPlus = 0
        if doubleClickMinus == 1:
            doubleClickMinus = 0
        if doubleClickMultiply == 1:
            doubleClickMultiply = 0
        if operation == 0:
            if howNumber == 1:
                calc.calculator()
            whatDo = '/'

    def squere(self):
        global numberOne, numberTwo, result, start
        if result == 0:
            result = numberOne * numberOne
            guiLabelResult.config(text = 'Equals:    ' + str(result))
            start = 1
        elif result != 0:
            result = result * result
            numberTwo = result
            guiLabelResult.config(text = 'Equals:    ' + str(result))

    def negate(self):
        global numberOne, numberTwo, result, start, firstNumber
        if firstOperation == 0:
            if numberOne > 0:
                numberOne = numberOne * -1
                guiLabelValues.config(text = 'Current number:    ' + str(numberOne))
            elif numberOne < 0:
                numberOne = numberOne * -1
                guiLabelValues.config(text = 'Current number:    ' + str(numberOne))
        elif firstOperation == 1:
            if numberTwo > 0:
                numberTwo = numberTwo * -1
                guiLabelValues.config(text = 'Current number:    ' + str(numberTwo))
            elif numberTwo < 0:
                numberTwo = numberTwo * -1
                guiLabelValues.config(text = 'Current number:    ' + str(numberTwo))
        if result > 0:
            result = result * -1
            guiLabelResult.config(text = 'Equals:    ' + str(result))
        elif result < 0:
            result = result * -1
            guiLabelResult.config(text = 'Equals:    ' + str(result))

    def percent(self):
        global numberOne, numberTwo, result, whatDo, start, plus, minus, multiply, division, doubleClickPlus, doubleClickMinus, doubleClickMultiply, doubleClickDivision
        if start == 0:
            if whatDo == '+':
                percent = float(numberOne) / 100
                result = numberOne + percent * numberTwo
                guiLabelResult.config(text = 'Equals:    ' + str(result))
                start = 1
                whatDo = ''
            elif whatDo == '-':
                percent = float(numberOne) / 100
                result = numberOne - percent * numberTwo
                guiLabelResult.config(text = 'Equals:    ' + str(result))
                start = 1
                whatDo = ''
            elif whatDo == '*':
                percent = float(numberOne) / 100
                result = percent * float(numberTwo)
                guiLabelResult.config(text = 'Equals:    ' + str(result))
                start = 1
                whatDo = ''
        if start == 1:
            if whatDo == '+':
                percent = float(result) / 100
                result = result + percent * numberTwo
                guiLabelResult.config(text = 'Equals:    ' + str(result))
                whatDo = ''
            elif whatDo == '-':
                percent = float(result) / 100
                result = result - percent * numberTwo
                guiLabelResult.config(text = 'Equals:    ' + str(result))
                whatDo = ''
            elif whatDo == '*':
                percent = float(result) / 100
                result = percent * float(numberTwo)
                guiLabelResult.config(text = 'Equals:    ' + str(result))
                whatDo = ''
        plus = 0
        minus = 0
        multiply = 0
        division = 0
        doubleClickPlus = 0
        doubleClickMinus = 0
        doubleClickMultiply = 0
        doubleClickDivision = 0

    def equal(self):
        global whatDo, howNumber, firstOperation, firstOrSecNumber, currentValue, operation, plus, minus, multiply, division, doubleClickPlus, doubleClickMinus, doubleClickMultiply, doubleClickDivision
        firstOperation = 1
        if operation == 0 and whatDo == '+':
            if doubleClickMinus == 1:
                whatDo = '-'
                doubleClickPlus = 0
                doubleClickMinus = 0
                doubleClickMultiply = 0
                doubleClickDivision = 0
            elif doubleClickMultiply == 1:
                whatDo = '*'
                doubleClickPlus = 0
                doubleClickMinus = 0
                doubleClickMultiply = 0
                doubleClickDivision = 0
            elif doubleClickDivision == 1:
                whatDo = '/'
                doubleClickPlus = 0
                doubleClickMinus = 0
                doubleClickMultiply = 0
                doubleClickDivision = 0
            if howNumber == 1:
                calc.calculator()
        elif operation == 0 and whatDo == '-':
            if doubleClickPlus == 1:
                whatDo = '+'
                doubleClickPlus = 0
                doubleClickMinus = 0
                doubleClickMultiply = 0
                doubleClickDivision = 0
            elif doubleClickMultiply == 1:
                whatDo = '*'
                doubleClickPlus = 0
                doubleClickMinus = 0
                doubleClickMultiply = 0
                doubleClickDivision = 0
            elif doubleClickDivision == 1:
                whatDo = '/'
                doubleClickPlus = 0
                doubleClickMinus = 0
                doubleClickMultiply = 0
                doubleClickDivision = 0
            if howNumber == 1:
                calc.calculator()
        elif operation == 0 and whatDo == '*':
            if doubleClickPlus == 1:
                whatDo = '+'
                doubleClickPlus = 0
                doubleClickMinus = 0
                doubleClickMultiply = 0
                doubleClickDivision = 0
            elif doubleClickMinus == 1:
                whatDo = '-'
                doubleClickPlus = 0
                doubleClickMinus = 0
                doubleClickMultiply = 0
                doubleClickDivision = 0
            elif doubleClickDivision == 1:
                whatDo = '/'
                doubleClickPlus = 0
                doubleClickMinus = 0
                doubleClickMultiply = 0
                doubleClickDivision = 0
            if howNumber == 1:
                calc.calculator()
        elif operation == 0 and whatDo == '/':
            if doubleClickPlus == 1:
                whatDo = '+'
                doubleClickPlus = 0
                doubleClickMinus = 0
                doubleClickMultiply = 0
                doubleClickDivision = 0
            elif doubleClickMinus == 1:
                whatDo = '-'
                doubleClickPlus = 0
                doubleClickMinus = 0
                doubleClickMultiply = 0
                doubleClickDivision = 0
            elif doubleClickMultiply == 1:
                whatDo = '*'
                doubleClickPlus = 0
                doubleClickMinus = 0
                doubleClickMultiply = 0
                doubleClickDivision = 0
            if howNumber == 1:
                calc.calculator()
        operation = 0
        currentValue = ''
        firstOperation = 0
        firstOrSecNumber = 0
        whatDo = ''
        howNumber = 0
        plus = 0
        minus = 0
        multiply = 0
        division = 0
        doubleClickPlus = 0
        doubleClickMinus = 0
        doubleClickMultiply = 0
        doubleClickDivision = 0

    def resetAll(self):
        global whatDo, howNumber, firstOperation, firstOrSecNumber, currentValue, operation, result, clickNumber, start, numberOne, numberTwo, plus, minus, multiply, division, doubleClickPlus, doubleClickMinus, doubleClickMultiply, doubleClickDivision
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
        plus = 0
        minus = 0
        multiply = 0
        division = 0
        doubleClickPlus = 0
        doubleClickMinus = 0
        doubleClickMultiply = 0
        doubleClickDivision = 0
        guiLabelResult.config(text = 'Equals:    ' + str(numberOne))
        guiLabelValues.config(text = 'Current number:    ' + str(result))

calc = Calculator()
varibles = CreateVaribles()
counterNumber = WhichNumber()
varibles.varibles()
number = Numbers()
operation = Operations()

guiLabelValues = tkinter.Label(gui, text = 'Current number:    ' + '0')
guiLabelValues.place(x=20, y=20)

guiLabelResult = tkinter.Label(gui, text = 'Equals:    ' + '0')
guiLabelResult.place(x=20, y=35)

guiButtonNegate = tkinter.Button(gui, text = "+/-", command = operation.negate, height = 3, width = 4)
guiButtonNegate.place(x=20, y=331)

guiButton0 = tkinter.Button(gui, text = "0", command = number.number0, height = 3, width = 4)
guiButton0.place(x=85, y=331)

guiButtonComma = tkinter.Button(gui, text = ",", command = number.dot, height = 3, width = 4)
guiButtonComma.place(x=150, y=331)

guiButtonEqual = tkinter.Button(gui, text = "=", command = operation.equal, height = 3, width = 4)
guiButtonEqual.place(x=215, y=331)

guiButton1 = tkinter.Button(gui, text = "1", command = number.number1, height = 3, width = 4)
guiButton1.place(x=20, y=270)

guiButton2 = tkinter.Button(gui, text = "2", command = number.number2, height = 3, width = 4)
guiButton2.place(x=85, y=270)

guiButton3 = tkinter.Button(gui, text = "3", command = number.number3, height = 3, width = 4)
guiButton3.place(x=150, y=270)

guiButtonPlus = tkinter.Button(gui, text = "+", command = operation.plus, height = 3, width = 4)
guiButtonPlus.place(x=215, y=270)

guiButton4 = tkinter.Button(gui, text = "4", command = number.number4, height = 3, width = 4)
guiButton4.place(x=20, y=209)

guiButton5 = tkinter.Button(gui, text = "5", command = number.number5, height = 3, width = 4)
guiButton5.place(x=85, y=209)

guiButton6 = tkinter.Button(gui, text = "6", command = number.number6, height = 3, width = 4)
guiButton6.place(x=150, y=209)

guiButtonMinus = tkinter.Button(gui, text = "-", command = operation.minus, height = 3, width = 4)
guiButtonMinus.place(x=215, y=209)

guiButton7 = tkinter.Button(gui, text = "7", command = number.number7, height = 3, width = 4)
guiButton7.place(x=20, y=148)

guiButton8 = tkinter.Button(gui, text = "8", command = number.number8, height = 3, width = 4)
guiButton8.place(x=85, y=148)

guiButton9 = tkinter.Button(gui, text = "9", command = number.number9, height = 3, width = 4)
guiButton9.place(x=150, y=148)

guiButtonPercent = tkinter.Button(gui, text = "%", command = operation.percent, height = 3, width = 4)
guiButtonPercent.place(x=20, y=87)

guiButtonSquere = tkinter.Button(gui, text = "Squere", command = operation.squere, height = 3, width = 4)
guiButtonSquere.place(x=85, y=87)

guiButtonC = tkinter.Button(gui, text = "C", command = operation.resetAll, height = 3, width = 4)
guiButtonC.place(x=150, y=87)

guiButtonDivision = tkinter.Button(gui, text = "/", command = operation.division, height = 3, width = 4)
guiButtonDivision.place(x=215, y=87)

guiButtonMultiply = tkinter.Button(gui, text = "x", command = operation.multiply, height = 3, width = 4)
guiButtonMultiply.place(x=215, y=148)

gui.mainloop()
