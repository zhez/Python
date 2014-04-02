import turtle
import time
t=turtle.Pen()

def mysqu(size):
	for x in range (4):
		t.forward(size)
		t.left(90)

t.reset()

i=raw_input('Please into squ number :')
l=raw_input('please into squ long :')


for x in range(int(1),int(i)+1):
	mysqu(l * x)

time.sleep(10)