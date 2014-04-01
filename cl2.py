class Animal:
	def __init__(self,species,number_of_legs,color):
		self.species=species
		self.number_of_legs=number_of_legs
		self.color=color



import copy
harry=Animal('hippogriff',6,'pink')
marry=copy.copy(harry)
print(harry.color)
print(marry.color)