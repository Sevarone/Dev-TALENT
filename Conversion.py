# -*- coding: utf-8 -*-
import os
''' Conversion project '''
__developer__ = 'Tevarone'
__date__ = '20/4/2017'
class Conversion:
	def __init__(self):
		self.convert_from = ['Tokens', 'Chars']
		self.convert_to = ['Tokens', 'Chars']
				
	def convert(self, mode):
		os.system('color b')
		os.system('title Conversion v1.0')
		print('CONVERSION V1.0').center(90)
		print('Conversions:\n[1]: Chars\n[2]: Tokens')
		self.input = input()
		self.input('Type conversion mode: ')
		if mode in ['1', 'Chars']:
			packet = self.input('[CHAR]: ') # convert char to token
			print(ord(pakcet)
		elif mode in ['2', 'Tokens']:
			packet = self.input('[TOKEN]: ') # convert token to char
			print(chr(str(packet))
					
if __name__ == '__main__':
		Conversion()
		convert()
