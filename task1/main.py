
from tkinter import *
import tkinter.messagebox

#выход из приложения
def exit_(event):
    root.destroy()

#справка
def pomosh(event):
    tkinter.messagebox.showinfo("Справка по игре.",
                                "F1 - Инфа.\n"+
                                "F12 - Новая игра.\n"+
                                "Ecs - выход из игры.\n"+
                                "Автор Сечак.Е.Н\n"
                                "группа №1652\n")

#начать занаво
def begin(event):
    global butn
    global field
    global numButton
    for b in butn:
        b.config(bg="white smoke",text = '')
    field = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    numButton = []
    
       

#логика приложения
def logik():
    global field
    global numButton
    if len(numButton) == 9:
        tkinter.messagebox.showinfo("Конец игры", "  Ничья!!!  ")
        begin(None)
    else:
        end = False
        if field[0] == field[1] == field[2] > 0:
            winner = field[0]
            end = True
        elif field[3] == field[4] == field[5] > 0:
            winner = field[3]
            end = True
        elif field[6] == field[7] == field[8] > 0:
            winner = field[6]
            end = True
        elif field[0] == field[3] == field[6] > 0:
            winner = field[0]
            end = True
        elif field[1] == field[4] == field[7] > 0:
            winner = field[1]
            end = True
        elif field[2] == field[5] == field[8] > 0:
            winner = field[2]
            end = True
        elif field[0] == field[4] == field[8] > 0:
            winner = field[0]
            end = True
        elif field[2] == field[4] == field[6] > 0:
            winner = field[2]
            end = True
        if end:
            if winner == 1:
                user = "Нолик"
            elif winner == 2:
                user = "Крестик"
            tkinter.messagebox.showinfo("Конец игры", "Выиграл " + user)
            begin(None)

#нажатие на кнопки
def click(button, num):
    global numButton
    if num not in numButton:
        global XO
        if XO == 1:
            button.config(text = 'O')
            field[num] = XO
            XO = 2
        else:
            button.config(text = 'X')
            field[num] = XO
            XO = 1
        numButton.append(num)
        logik()


field = [0, 0, 0, 0, 0, 0, 0, 0, 0] #список значений 1 или 2
XO = 1#крестик - 1, нолик - 2
numButton = [] #список нажатых кнопок


root = Tk()
root.title("Крестики-нолики")
root.geometry("240x258")


ris0 = Button(root, width=10, height=5, command=lambda:click(ris0, 0))
ris0.place(x=0, y=0)
ris1 = Button(root, width=10, height=5, command=lambda:click(ris1, 1))
ris1.place(x=81, y=0)
ris2 = Button(root, width=10, height=5, command=lambda:click(ris2, 2))
ris2.place(x=162, y=0)

ris3 = Button(root, width=10, height=5, command=lambda:click(ris3, 3))
ris3.place(x=0, y=86)
ris4 = Button(root, width=10, height=5, command=lambda:click(ris4, 4))
ris4.place(x=81, y=86)
ris5 = Button(root, width=10, height=5, command=lambda:click(ris5, 5))
ris5.place(x=162, y=86)

ris6 = Button(root, width=10, height=5, command=lambda:click(ris6, 6))
ris6.place(x=0, y=172)
ris7 = Button(root, width=10, height=5, command=lambda:click(ris7, 7))
ris7.place(x=81, y=172)
ris8 = Button(root, width=10, height=5, command=lambda:click(ris8, 8))
ris8.place(x=162, y=172)

butn = [ris0, ris1, ris2, ris3, ris4, ris5, ris6, ris7, ris8]

root.mainloop()