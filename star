import turtle


turtle.Screen().bgcolor("red")
turtle.Screen().setup(300,400,0,0)
polygony=turtle.Turtle()
for i in range(0,5,1):
    polygony.forward(150)
    polygony.right(144)

turtle.goto(100,100)
    
for i in range(0,10,1):
    polygony.forward(150)
    polygony.right(144)

turtle.done() 


