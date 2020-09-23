#A test function to see how you can profile code for speedups
#Run with:
#python -m cProfile faster.py

import time

def waithere():
	print("waiting for 1 second")
	time.sleep(1)

def add2(a=0,b=0):
	print("adding ", a, "and", b)
	return(a+b)

def main():
	print("Hello, try timing some parts of this code!")

	waithere()
	
	add2(4,7)

	add2(3,1)


if __name__=='__main__':
	main()