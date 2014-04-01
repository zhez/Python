import turtle
import time
t=turtle.Pen()

def mysqu(size):
	for x in range (1,5):
		t.forward(size)
		t.left(90)

t.reset()

print('Please into squ number')
i=input()
print('please into squ long')
l=input()

for x in range(1,i+1):
	mysqu(l * x)

time.sleep(10)