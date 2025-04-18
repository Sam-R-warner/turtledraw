# TurtleDrawLite
#By: Samuel Warner
#Credits: Eric Pogue, Dr. Ray Klump, Chat-GPT
#All rights reserved.
#Note: Many more examples can be found by searching "python turtle example".
# https://michael0x2a.com/blog/turtle-examples
# https://realpython.com/beginners-guide-python-turtle


import turtle

print("Turtle Draw Starting...")

tddata = open("turtledrawtext.text", "r")

line = tddata.readline()

while line:
	print(line, end='')
	parts = line.split(' ')
	print(parts)
	line = tddata.readline()

print('End')