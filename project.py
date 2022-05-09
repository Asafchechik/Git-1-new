from datetime import date
from tkinter import *
from tkinter import ttk
import datetime as datetime

win = Tk()
win.geometry("750x450")
win.title('Rock Paper Scissors...')


def rock():
    calc("Rock")


def paper():
    calc("Paper")


def scissor():
    calc("Scissor")


def calc(player_choice):
    import random
    computer_options = {'0': 'Rock', '1': 'Paper', '2': 'Scissor'}
    computer_choice = computer_options[str(random.randint(0, 2))]
    if player_choice == computer_choice:
        match_result = "Match Draw"
    elif (player_choice == 'Rock' and computer_choice == 'Scissor') \
            or (player_choice == 'Paper' and computer_choice == 'Rock') \
            or player_choice == 'Scissor' and computer_choice == 'Paper':
        match_result = "Player Win"
    elif (computer_choice == 'Rock' and player_choice == 'Scissor') \
            or (computer_choice == 'Paper' and player_choice == 'Rock') \
            or computer_choice == 'Scissor' and player_choice == 'Paper':
        match_result = "Computer Win"

    label.config(text=match_result)
    l1.config(text=player_choice)
    l3.config(text=computer_choice)
    button_disable()
    writeToCSV(computer_choice, player_choice, match_result)


def button_disable():
    b1.config(state="disabled")
    b2.config(state="disabled")
    b3.config(state="disabled")


def writeToCSV(computer_choice, player_choice, match_result):
    import csv
    f = open(r'C:\Users\User\PycharmProjects\GIT 1\results game.csv', 'a', newline='')
    writer = csv.writer(f)
    writer.writerow([datetime.datetime.today(), computer_choice, player_choice, match_result])
    f.close()


def reset():
    b1.config(state="active")
    b2.config(state="active")
    b3.config(state="active")
    l1.config(text="Player")
    l3.config(text="Computer")
    label.config(text="")


labelframe = LabelFrame(win, text="Rock Paper Scissor", font=('Century 20 bold'), labelanchor="n", bd=5, bg="khaki3",
                        width=600, height=450, cursor="target")
labelframe.pack(expand=True, fill=BOTH)

l1 = Label(labelframe, text="Player", font=('Helvetica 18 bold'))
l1.place(relx=.18, rely=.1)

l2 = Label(labelframe, text="VS", font=('Helvetica 18 bold'), bg="khaki3")
l2.place(relx=.45, rely=.1)

l3 = Label(labelframe, text="Computer", font=('Helvetica 18 bold'))
l3.place(relx=.65, rely=.1)

label = Label(labelframe, text="", font=('Coveat', 25, 'bold'), bg="khaki3")
label.pack(pady=150)

b1 = Button(labelframe, text="Rock", font=10, width=7, command=rock)
b1.place(relx=.25, rely=.62)
b2 = Button(labelframe, text="Paper", font=10, width=7, command=paper)
b2.place(relx=.41, rely=.62)
b3 = Button(labelframe, text="Scissor", font=10, width=7, command=scissor)
b3.place(relx=.58, rely=.62)

reset = Button(labelframe, text="Reset", bg="OrangeRed3", fg="white", width=7, font=10, command=reset)
reset.place(relx=.8, rely=.62)

win.mainloop()
