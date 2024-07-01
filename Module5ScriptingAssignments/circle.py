import turtle
import math

def drawCircle(t, x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.setheading(0)
    
    circumference = 2.0 * math.pi * radius
    step_length = circumference / 120.0
    step_angle = 3
    
    for _ in range(120):
        t.forward(step_length)
        t.left(step_angle)

def main():
    screen = turtle.Screen()
    t = turtle.Turtle()
    
    drawCircle(t, 0, 0, 100)
    
    screen.mainloop()

if __name__ == "__main__":
    main()
