import turtle

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch(t, order-1, size)
        t.left(60)
        koch(t, order-1, size)
        t.right(120)
        koch(t, order-1, size)
        t.left(60)
        koch(t, order-1, size)

def drawKochSnowflake(t, order, size):
    for _ in range(3):
        koch(t, order, size)
        t.right(120)

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    t = turtle.Turtle()
    t.speed(0)

    drawKochSnowflake(t, 2, 300)

    screen.mainloop()

if __name__ == "__main__":
    main()
