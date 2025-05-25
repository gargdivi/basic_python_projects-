from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Scores and round tracking
userscore = 0
pcscore = 0
rounds_played = 0
round_limit = 0

# Initialize main window
root = Tk()
root.title('Rock Paper Scissor Game')
root.wm_iconbitmap("images/play.png")
root.geometry('650x750')
root.maxsize(650, 750)
root.minsize(650, 450)

rock = Button()
paper = Button()
scissor = Button()
L1 = Label()
pcchose = Label()
L2 = Label()
L3 = Label()

def enter(event): rock.config(bg='black', fg='white')
def leave(event): rock.config(bg='white', fg='black')
def enter1(event): paper.config(bg='black', fg='white')
def leave1(event): paper.config(bg='white', fg='black')
def enter2(event): scissor.config(bg='black', fg='white')
def leave2(event): scissor.config(bg='white', fg='black')

def entergame(event):
    if nameinp.get().strip() != "" and roundinp.get().isdigit():
        maingame()

def check_game_end():
    global rounds_played, round_limit
    if rounds_played >= round_limit:
        if userscore > pcscore:
            winner = f"{nameinp.get()} wins!"
        elif pcscore > userscore:
            winner = "Computer wins!"
        else:
            winner = "It's a tie!"
        messagebox.showinfo("Game Over", f"Rounds completed!\nFinal Score:\n{nameinp.get()}: {userscore}\nComputer: {pcscore}\n{winner}")
        root.destroy()

def maingame():
    global userscore, pcscore, nameinp, rock, paper, scissor, L2, L3, round_limit, roundinp, rounds_played

    round_limit = int(roundinp.get())
    rounds_played = 0

    root.geometry('650x750')
    name.destroy()
    f1.destroy()
    inpname.destroy()
    sub.destroy()
    roundlabel.destroy()
    roundinp.destroy()

    L2 = Label(text=f"{nameinp.get()} Score: {userscore}", bg='#4834DF', fg='#ffffff', borderwidth=5, relief=RAISED,
               font='Rockwell 13 bold', padx=4, pady=2)
    L2.grid(row=6, column=0, pady=15)
    L3 = Label(text=f"PC Score: {pcscore}", bg='#4834DF', fg='white', borderwidth=5, relief=RAISED,
               font='Rockwell 13 bold', padx=4, pady=2)
    L3.grid(row=7, column=0, pady=15)

    def click(event):
        global userscore, pcscore, L1, pcchose, L2, L3, rounds_played

        L1.grid_forget()
        pcchose.destroy()

        val = event.widget.cget('text')
        pc_opt = random.choice(['Rock', 'Paper', 'Scissor'])

        pcchose = Label(text=f'PC Opted: {pc_opt}', font='lucida 15 bold', bg='black', fg='red')
        pcchose.grid(row=6, column=1, pady=15)

        if val == pc_opt:
            L1 = Label(text="It's A Tie", font='lucida 15 bold', bg='black', fg='gold')
        elif (val == 'Rock' and pc_opt == 'Scissor') or \
             (val == 'Paper' and pc_opt == 'Rock') or \
             (val == 'Scissor' and pc_opt == 'Paper'):
            userscore += 1
            L1 = Label(text=f"{nameinp.get()} Won", font='lucida 15 bold', bg='black', fg='gold')
        else:
            pcscore += 1
            L1 = Label(text='PC Won', font='lucida 15 bold', bg='black', fg='gold')

        L1.grid(row=7, column=1, pady=15)
        L2.config(text=f"{nameinp.get()} Score: {userscore}")
        L3.config(text=f"PC Score: {pcscore}")

        rounds_played += 1
        check_game_end()

    head = Label(text='Rock Paper Scissor', font='arial 35 bold', bg='black', fg='white')
    head.grid(columnspan=2, row=0, ipadx=70, padx=33, pady=10)
    playerone = Label(text=f'Player 1 : {nameinp.get()}', font='lucida 16')
    playerone.grid(row=2, column=0)
    playertwo = Label(text=f'Player 2 : Computer', font='lucida 16')
    playertwo.grid(row=2, column=1)

    rock = Button(text='Rock', font='comicsansms 14 bold', height=1, width=7, bg='white')
    rock.grid(row=3, column=0, pady=15)
    rock.bind('<Enter>', enter)
    rock.bind('<Leave>', leave)
    rock.bind('<Button-1>', click)

    paper = Button(text='Paper', font='comicsansms 14 bold', height=1, width=7, bg='white')
    paper.grid(row=4, column=0)
    paper.bind('<Enter>', enter1)
    paper.bind('<Leave>', leave1)
    paper.bind('<Button-1>', click)

    scissor = Button(text='Scissor', font='comicsansms 14 bold', height=1, width=7, bg='white')
    scissor.grid(row=5, column=0, pady=15)
    scissor.bind('<Enter>', enter2)
    scissor.bind('<Leave>', leave2)
    scissor.bind('<Button-1>', click)

    Button(text='Rock', font='comicsansms 14 bold', height=1, width=7).grid(row=3, column=1, pady=15)
    Button(text='Paper', font='comicsansms 14 bold', height=1, width=7).grid(row=4, column=1)
    Button(text='Scissor', font='comicsansms 14 bold', height=1, width=7).grid(row=5, column=1, pady=15)

    btnclose = Button(text='Close Game', command=root.destroy, bg='green', font='arial 10 bold')
    btnclose.place(x=300, y=410)

# Home screen
f1 = Frame(root)
img = Image.open('images/symbols.png')
img = img.resize((650, 450), Image.LANCZOS)
pic = ImageTk.PhotoImage(img)
Lab = Label(f1, image=pic)
Lab.pack()
f1.pack()

name = Label(root, text='Enter Your Name :', font='arial 15 bold')
name.place(x=262, y=250)

nameinp = StringVar()
inpname = Entry(root, textvar=nameinp, font='arial 10 bold')
inpname.place(x=275, y=290)

# Round limit input
roundlabel = Label(root, text='Enter Number of Rounds :', font='arial 13 bold')
roundlabel.place(x=240, y=320)

roundinp = Entry(root, font='arial 10 bold')
roundinp.place(x=275, y=350)

inpname.bind('<Return>', entergame)
roundinp.bind('<Return>', entergame)

sub = Button(root, text="Let's Play", font='lucida 10 bold', bg='black', fg='white', command=maingame)
sub.place(x=305, y=390)

root.mainloop()
