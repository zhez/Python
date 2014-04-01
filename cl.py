class Things:
	pass
class Inanimate(Things):
    pass
class Animate(Things):
    pass
class Sidewalks(Inanimate):
    pass
class Animals(Animate):
    pass
class Mammals(Animate):
    pass
class Giraffes(Mammals):
    pass

class Animals(Animate):
    def breathe(self):
    	print('breatheing')
    def move(self):
    	print('moveing')
    def eat_food(self):
        print('eating food')

class Mammals(Animals):
	def feed_young_with_milk(self):
		print('feeding young')

class Giraffes(Mammals):
	def eat_leaves_from_trees(self):
		print('eating leaves')
	def __init__(self,spots):
		self.Giraffes_spots=spots

yz=Giraffes(100)
zy=Giraffes(150)
print(yz.Giraffes_spots)
print(zy.Giraffes_spots)