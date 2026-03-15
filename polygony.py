import turtle


turtle.Screen().bgcolor("red")
turtle.Screen().setup(300,400,0,0)
polygony=turtle.Turtle()
for i in range(0,8,1):
    polygony.forward(150)
    polygony.right(45)
    polygony.left(90)

    
turtle.done() 
