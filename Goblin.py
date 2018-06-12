#Make Goblin a child/subclass

from character import Character
class Goblin(Character):
	def __init__(self):
		#we use the super! method the super method is the same 
		#as running the parent __init__ method
		super(Goblin, self).__init__('Goblin', 6, 2)
	def doALittle(self):
		print "The goblin has done a dance. You are mesmerized."