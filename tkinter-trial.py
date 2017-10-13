#! /usr/bin/env python3
from tkinter import *
from tkinter import messagebox
from tictactoe import TicTacToe


tk = Tk()
tk.title('Tic Tac Toe')

player1 = 'X'
player2 = 'O'
click = True


def button_clicked(buttons): 
	global click
	if buttons['text'] == '' and click == True:
		buttons['text'] = 'X'
		click = False
		if(button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
		button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
		button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
		button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
		button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
		button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
		button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
		button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X'):
			messagebox.showinfo('Player 1: X', 'You Win! Game Over!')
			tk.destroy()

	elif buttons['text'] == '' and click == False:
		buttons['text'] = 'O'
		click = True
		if(button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
		button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
		button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
		button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
		button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
		button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
		button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
		button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O'):
			messagebox.showinfo('Player 2: O', 'You Win! Game Over!')
			tk.destroy()

buttons = StringVar()
button1 = Button(tk,text='',font=('Times bold', 10),height = 10,width = 20,command=lambda:button_clicked(button1))
button1.grid(row=1, column=0,sticky = S+N+E+W)

button2 = Button(tk,text='',font=('Times 9 bold'),height = 10,width = 20,command=lambda:button_clicked(button2))
button2.grid(row=1, column=1,sticky = S+N+E+W)

button3 = Button(tk,text='',font=('Times 9 bold'),height = 10,width = 20,command=lambda:button_clicked(button3))
button3.grid(row=1, column=2,sticky = S+N+E+W)

button4 = Button(tk,text='',font=('Times 9 bold'),height = 10,width = 20,command=lambda:button_clicked(button4))
button4.grid(row=2, column=0,sticky = S+N+E+W)

button5 = Button(tk,text='',font=('Times 9 bold'),height = 10,width = 20,command=lambda:button_clicked(button5))
button5.grid(row=2, column=1,sticky = S+N+E+W)

button6 = Button(tk,text='',font=('Times 9 bold'),height = 10,width = 20,command=lambda:button_clicked(button6))
button6.grid(row=2, column=2,sticky = S+N+E+W)

button7 = Button(tk,text='',font=('Times 9 bold'),height = 10,width = 20,command=lambda:button_clicked(button7))
button7.grid(row=3, column=0,sticky = S+N+E+W)

button8 = Button(tk,text='',font=('Times 9 bold'),height = 10,width = 20,command=lambda:button_clicked(button8))
button8.grid(row=3, column=1,sticky = S+N+E+W)

button9 = Button(tk,text='',font=('Times 9 bold'),height = 10,width = 20,command=lambda:button_clicked(button9))
button9.grid(row=3, column=2,sticky = S+N+E+W)

	
tk.mainloop()