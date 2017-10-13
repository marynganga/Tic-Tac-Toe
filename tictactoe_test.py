import unittest
from tictactoe import TicTacToe

player1 = 'X'
player2 = 'O'
click = True

class TestTicTacToe(unittest.TestCase):
	"""
	docstring for TestTicTacToe
	"""
	
	# def SetUp(self):
	# 	global player1
	# 	global player2
	# 	global click

	def test_current_player(self):
		global player1
		global player2
		global click
		self.assertTrue(True, TicTacToe.current_player(player1))

	def test_button_clicked(self):
		global click
		if click == True:
			click = False
			return click
		self.assertFalse(False, TicTacToe.button_clicked(click))
		if click == False:
			click = True
			return click
		self.assertFalse(True, TicTacToe.button_clicked(click))
		


if __name__ == '__main__':
		unittest.main(verbosity=2)	