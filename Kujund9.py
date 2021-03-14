#Erika Laherand ITT20
#Turtle kujund 9

import turtle
import random
#ekraani seaded
aken=turtle.Screen()
aken.setup(500,500)
aken.bgcolor("yellow")
aken.title("Kujund 9")

x=90
a=100
varvid=["lime","red","orange","blue","green"]

def ruut(varv,x,a):
   for i in range(3):
      turtle.color(varv)
      turtle.fd(a)
      turtle.lt(x)
      
for j in range(4):
   for i in range(4):
      ruut("black",x,a)
      turtle.rt(2*x)
   turtle.fd(a)
   turtle.rt(x)
   turtle.fd(a)
   turtle.rt(2*x)



turtle.exitonclick()

