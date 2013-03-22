# This is where Exercise 5.4 goes
# Name: Tamar Schanfeld
def is_triangle(a,b,c):
	if a > b + c or b > a + c or c > a + b:
		print "No"
	else:
		print "Yes"


def is_triangleinput():
	a = int(raw_input('Enter first stick length: '))
	b = int(raw_input('Enter second stick length: '))
	c = int(raw_input('Enter third stick length: '))
	is_triangle(a,b,c)

is_triangleinput
