import turtle
import time
t=turtle.Pen()

t1=time.time()

t.up()
t.backward(300)
t.down()

def drawbox ():
	for x in range(0,4):
		t.color(1,0,0)
		t.begin_fill()
		t.forward(50)
		t.right(90)
		t.end_fill()

def drawx ():
	    t.up()
	    t.forward(60)
	    t.down()

def drawline (i):
    for x in range(0,i):
		drawbox()
		drawx()

def reline ():
	t.up()
        t.right(90)
        t.forward(60)
        t.left(90)
        t.backward(240)
        t.down()

for x in range(0,4):
    drawline(4)
    reline()

t2=time.time()
print('it took %s seconds' % ((t2-t1)*2))