# -*- coding: utf-8 -*-
import os, time
# Simple Conversion Type Script(Python)
__developer__ = 'Tevar'
__date__ = '20/4/2017' # Day/Month/Year
class Conversion
	def __init__(self):
		title = 'CONVERSION V1.0' # Sub-Title script
		message_start = 'Choose one only from convert modes:\n[A]: From char to token.\n[B]: From token to char.' # Message script starting
		self.input = input('- ')
		os.system('title Conversion v1.0')
		os.system('color fb')
		print(str(title)).center(90)
		print(str(message_start))
		x = self.input('Mode: ')
		if x == 'A':
			convert_start(A) 
		elif x == 'B':
			convert_start(B)
		else:
			print('Please choose A or B')
			time.sleep(3)
			close()

	def convert_start(self, mode): # conversion start
		__char__, __token__ = 'A','B'
		if mode == __char__:
			packet = ord(self.input('[CHAR]: '))
			print('[TOKEN]: {0}'.format(packet))
			time.sleep(6)
			close()
		elif mode == __token__:
			packet = repr(self.input('[TOKEN]: '))
			print('[CHAR]: {0}'.format(packet))
			time.sleepww(6)
			close()
      
if __name__ == '__main__':
	Conversion()
