import turtle
import random
t = turtle.Pen()

t.color('grey')
t.shape('turtle')
t.speed(5)
t.penup()

# sun
t.goto(-10,0)
t.begin_fill()
t.fillcolor('gold')
t.circle(100)
t.end_fill()
t.penup()

# draw mountains
t.goto(-485,0)
t.begin_fill()
t.fillcolor('grey')
t.pendown()
t.left(60)
t.forward(470)
t.right(120)
t.forward(470)
t.left(120)
t.forward(470)
t.right(120)
t.forward(470)
t.end_fill()

#draw green land
t.penup()
t.goto(-485,0)
t.begin_fill()
t.left(60)
t.fillcolor('green')
t.pendown()
t.forward(970)
t.right(90)
t.forward(500)
t.right(90)
t.forward(970)
t.right(90)
t.forward(500)
t.right(90)
t.end_fill()

#tree bark
t.color('saddle brown')
t.penup()
t.goto(420,100)
t.pendown()
t.begin_fill()
t.fillcolor('saddle brown')
t.forward(100)
t.right(90)
t.forward(500)
t.right(90)
t.forward(100)
t.right(90)
t.forward(500)
t.right(90)
t.end_fill()
t.penup()

# tree leaf 1
t.color('dark green')
t.goto(300,-100)
t.pendown()
t.begin_fill()
t.fillcolor('dark green')
t.forward(400)
t.left(120)
t.forward(400)
t.left(120)
t.end_fill()
t.penup()

# tree leaf 2
t.goto(470,250)
t.pendown()
t.begin_fill()
t.fillcolor('dark green')
t.forward(250)
t.left(120)
t.forward(250)
t.left(120)
t.end_fill()
t.penup()

# tree leaf 3
t.goto(590,150)
t.pendown()
t.begin_fill()
t.fillcolor('dark green')
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.end_fill()
t.penup()

#lake 
t.begin_fill()
t.fillcolor('blue')
t.color('blue')
def flatoval(r):               
    t.right(45)
    for loop in range(2):
        t.circle(r,90)
        t.circle(r/8,90)
t.goto(-300,-250)
flatoval(400)
t.end_fill()

#move the turtle near lake
t.penup()
t.speed(1)
t.goto(-100,-100)
t.color('peru')
increase = (3,3,3)
t.turtlesize(*increase)
t.right(30)
for x in range(1,38):
    t.forward(100)
    t.left(175)













