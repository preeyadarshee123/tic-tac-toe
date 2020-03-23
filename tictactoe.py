import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
import random

root=tk.Tk()
root.title("Tic Tac Toe")
frame=tk.Frame(root)
buttons=[]
players=[]
def reset():
    for i in range(3):
        for j in range(3):
            b[i][j].config(text=" ",state="normal")
    buttons[0].config(state="normal")
    buttons[0].config(command=toss)

def check(i,j):
    global flag
    for k in ['O','X']:
        if not (k==flag):
            flag=k
            break
    b[i][j].config(state="disabled",text=flag,relief="groove",disabledforeground="green")
    for i in range(3):
            if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]=='O' or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]=='O'):
                    messagebox.showinfo("Congrats!!","'"+players[0]+"' has won")
                    reset()

    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]=='O' or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]=='O'):
        messagebox.showinfo("Congrats!!","'"+players[0]+"' has won")
        reset()

    for i in range(3):
            if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]=='X' or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]=='X'):
                    messagebox.showinfo("Congrats!!","'"+players[1]+"' has won")
                    reset()
                    
    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]=='X' or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]=='X'):
        messagebox.showinfo("Congrats!!","'"+players[1]+"' has won")
        reset()
        
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]=="disabled"):
        messagebox.showinfo("Tied!!","The match ended in a draw")
        reset()

def build_game():
    frame2.pack(expand=True)

def toss():
    global a
    a=random.randint(0,100000)
    a=a%2
    buttons[0].config(state="disabled")
    p1=entry1.get()
    p2=entry2.get()
    if a==1:
        messagebox.showinfo(p1+" won the toss")
        players.append(p1)
        players.append(p2)
    else:
        messagebox.showinfo(p2+" won the toss")
        players.append(p2)
        players.append(p1)
    build_game()


def play():
    button1['state']=tk.DISABLED
    frame_l=tk.Frame(root)
    tk.Label(frame_l,text="Let's Toss. !! :D",bg="black",fg="green",font=myFont).grid(row=1,column=2)
    name="b1"
    b1=tk.Button(frame_l,text="Click to Toss",highlightbackground="yellow",font=myFont,command=lambda :[ toss() ])
    buttons.append(b1)
    b1.grid(row=2,column=2,padx=20,pady=20   )
    frame_l.pack()

def button(frame):
    b=tk.Button(frame,padx=1,fg="green",width=3,text="   ",font=('arial',20,'bold'),relief="sunken",highlightbackground="skyblue",bd=1)
    return b

flag='X'
myFont=font.Font(size=20)
label1=tk.Label(frame,text="Player 1 Name:- ",bg="black",fg="green",font=myFont)
label1.grid(row=1,column=1,padx=5,pady=5)
entry1=tk.Entry(frame,bg="black",fg="green",font=myFont)
entry1.grid(row=1,column=2,padx=5,pady=5)
label2=tk.Label(frame,text="Player 2 Name:- ",bg="black",fg="green",font=myFont)
label2.grid(row=2,column=1)
entry2=tk.Entry(frame,bg="black",fg="green",font=myFont)
entry2.grid(row=2,column=2)
button1=tk.Button(frame,text="Submit",highlightbackground="yellow",font=myFont,command=lambda :[ play() ])
button1.grid(row=3,column=2,sticky="w",padx=5,pady=5)
frame.pack(fill=tk.BOTH,expand=True)
frame2=tk.Frame(root,bg="black")
b=[[],[],[]]
for i in range(3):
        for j in range(3):
                b[i].append(button(frame2))
                b[i][j].config(command= lambda row=i,col=j:check(row,col))
                b[i][j].grid(row=i,column=j)
root.mainloop()