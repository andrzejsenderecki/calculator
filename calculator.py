import tkinter

gui = tkinter.Tk()
gui.geometry('293x405')
gui.title('Calculator')

guiButtonNegate = tkinter.Button(gui, text = "NEG", height = 3, width = 7)
guiButtonNegate.place(x=20, y=331)

guiButton0 = tkinter.Button(gui, text = "0", height = 3, width = 7)
guiButton0.place(x=85, y=331)

guiButtonComma = tkinter.Button(gui, text = ",", height = 3, width = 7)
guiButtonComma.place(x=150, y=331)

guiButtonEqual = tkinter.Button(gui, text = "=", height = 3, width = 7)
guiButtonEqual.place(x=215, y=331)

guiButton1 = tkinter.Button(gui, text = "1", height = 3, width = 7)
guiButton1.place(x=20, y=270)

guiButton2 = tkinter.Button(gui, text = "2", height = 3, width = 7)
guiButton2.place(x=85, y=270)

guiButton3 = tkinter.Button(gui, text = "3", height = 3, width = 7)
guiButton3.place(x=150, y=270)

guiButtonPlus = tkinter.Button(gui, text = "+", height = 3, width = 7)
guiButtonPlus.place(x=215, y=270)

guiButton4 = tkinter.Button(gui, text = "4", height = 3, width = 7)
guiButton4.place(x=20, y=209)

guiButton5 = tkinter.Button(gui, text = "5", height = 3, width = 7)
guiButton5.place(x=85, y=209)

guiButton6 = tkinter.Button(gui, text = "6", height = 3, width = 7)
guiButton6.place(x=150, y=209)

guiButtonMinus = tkinter.Button(gui, text = "-", height = 3, width = 7)
guiButtonMinus.place(x=215, y=209)

guiButton7 = tkinter.Button(gui, text = "7", height = 3, width = 7)
guiButton7.place(x=20, y=148)

guiButton8 = tkinter.Button(gui, text = "8", height = 3, width = 7)
guiButton8.place(x=85, y=148)

guiButton9 = tkinter.Button(gui, text = "9", height = 3, width = 7)
guiButton9.place(x=150, y=148)

guiButtonMultiply = tkinter.Button(gui, text = "x", height = 3, width = 7)
guiButtonMultiply.place(x=215, y=148)

guiButtonPercent = tkinter.Button(gui, text = "%", height = 3, width = 7)
guiButtonPercent.place(x=20, y=87)

guiButtonSquere = tkinter.Button(gui, text = "Squere", height = 3, width = 7)
guiButtonSquere.place(x=85, y=87)

guiButtonC = tkinter.Button(gui, text = "C", height = 3, width = 7)
guiButtonC.place(x=150, y=87)

guiButtonDivision = tkinter.Button(gui, text = "/", height = 3, width = 7)
guiButtonDivision.place(x=215, y=87)

guiLabelResult = tkinter.Label(gui, text = "0")
guiLabelResult.place(x=20, y=35)

gui.mainloop()
