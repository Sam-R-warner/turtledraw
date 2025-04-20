# TurtleDrawLite
#By: Samuel Warner
#Credits: Eric Pogue, Dr. Ray Klump, Chat-GPT
#All rights reserved.
#Note: Many more examples
# https://michael0x2a.com/blog/turtle-examples
# https://realpython.com/beginners-guide-python-turtle


import turtle
import math

TEXTFILENAME = input("Enter the file name: ")
print(f"You entered: {TEXTFILENAME}")

import os
if not os.path.exists(TEXTFILENAME):
    print("Error: File not found.")
    exit()

print("Turtle Draw Starting...")

turtleScreen = turtle.Screen()
turtleScreen.setup(width=450, height=450)

turtleddata = turtle.Turtle()
turtleddata.speed(10)
turtleddata.penup()

def distance(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return math.hypot(dx, dy)

points = []
total_distance = 0

print("Reading text file line by line.")
turtleddataTEXT = open(TEXTFILENAME, "r")
line = turtleddataTEXT.readline()
while line:
	print(line, end='')
	parts = line.strip().split()

	if len(parts) == 3:
		color = parts[0]
		x = int(parts[1])
		y = int(parts[2])

		turtleddata.color(color)
		turtleddata.goto(x, y)
		turtleddata.pendown()
		points.append((x, y))

	if len(parts) == 1:
		turtleddata.penup()
		points.append(None)

	line = turtleddataTEXT.readline()

turtleddataTEXT.close()

prev = None
for pt in points:
	if pt is None:
		prev = None
	elif prev is not None:
		total_distance += distance(prev, pt)
		prev = pt
	else:
		prev = pt

turtleddata.penup()
turtleddata.hideturtle()
screen_width = turtleScreen.window_width()
screen_height = turtleScreen.window_height()
turtleddata.goto(screen_width // 2 - 200, -screen_height // 2 + 40)
turtleddata.write(f"Total distance: {total_distance:.2f}", align="left", font=("Arial", 12, "normal"))

print(f"\nTotal distance: {total_distance:.2f}")
print('End')

input("Press Enter to close the window...")
turtle.bye()