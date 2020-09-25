import turtle
window=turtle.Screen()
window.bgcolor("green")
tess=turtle.Turtle()
tess.color("blue")
tess.shape("turtle")
tess.stamp()

for i in range(12):
    tess.penup()
    tess.forward(100)
    tess.pendown()
    tess.forward(20)
    tess.penup()
    tess.forward(20)
    tess.stamp()
    tess.backward(140)
    tess.left(30)






window.exitonclick()