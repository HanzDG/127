#Name: Hanz De Guzman
#Email: hanz.deguzman87@myhunter.cuny.edu
#Date: September 13, 2021
#This program prints red psuedo hearts


import turtle               

turtle.colormode(255)        
tess = turtle.Turtle()        
tess.shape("turtle")        
tess.penup()
tess.backward(100)
tess.pendown()

for i in range(0,255,10):
     tess.forward(10)        
     tess.pensize(i)
     tess.color(255,255 - i,0)        

tess.penup()
tess.pensize(0)
tess.color(0, 0, 0)
tess.backward(260)
tess.right(90)
tess.pendown()

for i in range(0,255,10):
     tess.forward(10)        
     tess.pensize(i)        
     tess.color(255,255 - i,0)    
