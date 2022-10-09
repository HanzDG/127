#Name: Hanz De Guzman
#Email: hanz.deguzman87@myhunter.cuny.edu
#Date: September 24, 2021
#THis program prints Shades of yellow

import turtle				#Import the turtle drawing package

turtle.colormode(255)		#Allows colors to be given as 0...255
tess = turtle.Turtle()		#Create a turtle
tess.shape("turtle")		#Make it turtle shaped
tess.left(60)

#For 0,10,20,...,250
for i in range(0,255,10):
  tess.forward(10)		#Move forward
  tess.pensize(i)		#Set the drawing size to be i (larger each time)
  tess.color(255,255 - i,0)		#Set the yellow channel to be i (brighter each time)
  
tess.left(180)
tess.penup()                
tess.forward(260)
tess.pensize(1)             
tess.color(0,0,0)           
tess.right(120)
tess.pendown()      

for i in range(0,255,10):
  tess.forward(10)
  tess.pensize(i)
  tess.color(255,255 - i ,0)
