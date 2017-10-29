import turtle as t
t.shape("turtle")
t.up() 
t.fd(250)
t.lt(90)
t.fd(250)
t.lt(90)
t.down()
for x in range(4):
	t.fd(500)
	t.lt(90)

	
t.up()
t.home()
t.down()
t.seth(324)
while True:
	x=t.xcor()
	y=t.ycor()
	ang=t.heading()
	if -245<x<245 and -245<y<245:
		t.fd(10)
	else:
		if x>=245:
			t.seth(180-ang)
			t.fd(10)
		if y>=245:
			t.seth(-ang)
			t.fd(10)
		if x<=-245:
			t.seth(180-ang)
			t.fd(10)
		if y<=-245:
			t.seth(-ang)
			t.fd(10)
