#Erika Laherand
#Turtle

import turtle
import random
#ekraani seaded
aken=turtle.Screen()
aken.setup(300,500)
aken.bgcolor("yellow")
aken.title("Kodutöö")

x=90
a=100
b=a/2
c=b/2
varvid=["lime","red","orange","blue","green"]

def ruut(varv,x,a):
   for i in range(3):
       turtle.color(varv)
       turtle.lt(x)
       turtle.fd(a)
   turtle.lt(x) 

#suur maja
turtle.fd(b)
ruut("black",x,a)
turtle.fd(b)

#uks
turtle.fd(c)
ruut("red",x,b)

#edasi katust joonistama
turtle.penup()
turtle.fd(b+c)
turtle.lt(x)
turtle.fd(a)
turtle.pendown()
#katus
turtle.color(varvid[4])
turtle.lt(30)
turtle.fd(a)
turtle.lt(120)
turtle.fd(a)

turtle.exitonclick()

