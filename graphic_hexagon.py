import turtle
import colorsys

def Draw_shape():
    turtle.bgcolor("black")
    turtle.speed(0)
    turtle.width(2)

    for i in range(360):
        color=colorsys.hsv_to_rgb(i/36,1.0,1.0)
        turtle.pencolor(color)
        turtle.forward(i)
        turtle.right(60)
    turtle.done()

turtle.title("Colorful shape with turtle in FrontEndUni")
Draw_shape()