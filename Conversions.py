# -*- coding: utf-8
import os
__developer__ = 'Tevarone'
__date__ = '20/4/2017'
''' sample conversions '''
class Conversions:
  def __init__(self):
   swlf.input = raw_input('-')
   os.system('title Conversion v1.0')
   os.system('color fb')
   print('CONVERSION V1').center(90)
   print('Choose convert mode:\n[A]: From char to token\n[B]: From token to char')
   x = self.input('Mode:')
   if x == 'A':
    self.convert(A)
   elif x == 'B':
    self.convert(B)
	
  def convert(self, mode):
   if mode == 'A':
    packet = ord(self.input('[CHAR]:'))
    print('[TOKEN]: {0}'.format(str(packet)))
    close(6)
   elif mode == 'B':
    packet = chr(self.input('[TOKEN]:'))
    print('[CHAR]: {0}'.format(packet))
    close(6)
    
if __name__ == '__main':
 Conversions()
