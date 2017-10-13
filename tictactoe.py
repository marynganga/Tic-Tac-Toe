from tkinter import *
# tk = Tk()

player1 = 'X'
player2 = 'O'
click = True
class TicTacToe:
	'''
	class that updates the game board on each player's turn 
	'''
	
	def current_player(player):
		global player1
		global player2
		global click
		if player == player1:
			# tk.title('Player 1: X')
			return click == True
		else:
			# tk.title('Player 2: O')
			return click == False

	def button_clicked(buttons): 
		global click
		if buttons['text'] == '' and click == True:
			buttons['text'] = 'X'
			click = False
			# if(button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
			# button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
			# button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
			# button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
			# button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
			# button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
			# button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
			# button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X'):
			# 	messagebox.showinfo('Player X', 'You Win! Game Over!')

		elif buttons['text'] == '' and click == False:
			buttons['text'] = 'O'
			click = True
			# if(button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
			# button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
			# button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
			# button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
			# button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
			# button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
			# button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
			# button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O'):
			# 	messagebox.showinfo('Player O', 'You Win! Game Over!')
